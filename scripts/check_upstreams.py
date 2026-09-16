"""Report public upstream changes without activating downloaded instructions."""

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.parse import quote, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 1_048_576
MAX_SOURCES = 64


class AccessLimited(RuntimeError):
    pass


class NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        raise ValueError("Upstream redirects require a reviewed source change")


def read_public(url):
    parsed = urlsplit(url)
    if (parsed.scheme != "https" or parsed.hostname not in {"api.github.com", "raw.githubusercontent.com"}
            or parsed.username is not None or parsed.password is not None
            or parsed.port is not None or parsed.query or parsed.fragment):
        raise ValueError("Only reviewed public GitHub source URLs are permitted")
    opener = build_opener(ProxyHandler({}), NoRedirects())
    request = Request(url, headers={"User-Agent": "Hoplite-public-toolkit-maintenance/1.0"})
    try:
        with opener.open(request, timeout=25) as response:
            data = response.read(MAX_BYTES + 1)
    except HTTPError as error:
        if error.code in {403, 429}:
            raise AccessLimited(f"Public upstream access limited: HTTP {error.code}; no retry") from error
        raise
    if len(data) > MAX_BYTES:
        raise ValueError("Upstream source exceeds the byte limit")
    return data


def parse_source(url):
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.query or parsed.fragment or parsed.netloc != parsed.hostname:
        raise ValueError("Expected a public immutable GitHub source URL")
    parts = parsed.path.strip("/").split("/")
    if parsed.hostname == "github.com" and len(parts) >= 5 and parts[2] == "blob":
        owner, repo, _, commit, *path = parts
    elif parsed.hostname == "raw.githubusercontent.com" and len(parts) >= 4:
        owner, repo, commit, *path = parts
    else:
        raise ValueError("Unsupported upstream source URL")
    if (not all(re.fullmatch(r"[A-Za-z0-9_.-]+", value) and value not in {".", ".."} for value in [owner, repo])
            or not re.fullmatch(r"[a-f0-9]{40}", commit)
            or not path or any(value in {"", ".", ".."} or not re.fullmatch(r"[A-Za-z0-9_.-]+", value) for value in path)):
        raise ValueError("Pin the upstream repository, commit and plain file path")
    return f"{owner}/{repo}", commit, "/".join(path)


def inventory(root=ROOT):
    entries = json.loads((root / "docs/provenance/skills-export-manifest.json").read_text())["skills"]
    extra = root / "docs/provenance/additional-skills.json"
    if extra.exists():
        entries += json.loads(extra.read_text())["skills"]
    sources = defaultdict(set)
    local = []
    for entry in entries:
        urls = [url for attribution in entry.get("attributions", []) for url in attribution["source_urls"]]
        if not urls:
            local.append(entry["name"])
        for url in urls:
            sources[parse_source(url)].add(entry["name"])
    if len(sources) > MAX_SOURCES:
        raise ValueError("Review the source request budget before expanding the inventory")
    return sources, sorted(local)


def check_sources(root=ROOT, reader=read_public):
    sources, local = inventory(root)
    heads = {}
    records = []
    limited = None
    for (repository, commit, path), names in sorted(sources.items()):
        baseline_url = f"https://raw.githubusercontent.com/{repository}/{commit}/{path}"
        record = {"skills": sorted(names), "repository": repository, "path": path,
                  "reviewed_commit": commit, "reviewed_source_url": baseline_url}
        records.append(record)
        if limited:
            record.update(status="not_checked_due_to_limit", error=limited)
            continue
        try:
            if repository not in heads:
                metadata = json.loads(reader(f"https://api.github.com/repos/{repository}"))
                branch = metadata["default_branch"]
                ref = json.loads(reader(f"https://api.github.com/repos/{repository}/git/ref/heads/{quote(branch, safe='')}"))
                head = ref["object"]["sha"]
                if ref["object"]["type"] != "commit" or not re.fullmatch(r"[a-f0-9]{40}", head):
                    raise ValueError("The upstream head is not an exact Git commit")
                heads[repository] = {"branch": branch, "head": head}
            info = heads[repository]
            if "error" in info:
                raise ValueError(info["error"])
            current_url = f"https://raw.githubusercontent.com/{repository}/{info['head']}/{path}"
            record.update(default_branch=info["branch"], current_commit=info["head"], current_source_url=current_url)
            baseline = reader(baseline_url)
            record["reviewed_sha256"] = hashlib.sha256(baseline).hexdigest()
            try:
                current = baseline if commit == info["head"] else reader(current_url)
            except HTTPError as error:
                if error.code == 404:
                    record["status"] = "source_path_missing_review_required"
                    continue
                raise
            record["current_sha256"] = hashlib.sha256(current).hexdigest()
            record["status"] = "unchanged" if current == baseline else "changed_review_required"
        except AccessLimited as error:
            limited = str(error)
            record.update(status="access_limited", error=limited)
        except Exception as error:
            message = f"{type(error).__name__}: {error}"
            record.update(status="failed", error=message)
            if repository not in heads:
                heads[repository] = {"error": message}
    failed = {"failed", "access_limited", "not_checked_due_to_limit"}
    return {
        "schema_version": 1, "checked_at": datetime.now(timezone.utc).isoformat(),
        "activation": "Review only; no remote text is written into active skill roots",
        "authentication": "none", "local_skills_without_external_upstream": local,
        "sources": records, "passed": all(record["status"] not in failed for record in records),
        "needs_review": any(record["status"] != "unchanged" for record in records),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="reports/upstream-status.json")
    args = parser.parse_args()
    report = check_sources()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items() if key != "sources"}, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
