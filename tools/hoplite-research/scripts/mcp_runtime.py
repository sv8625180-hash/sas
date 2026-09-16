"""Shared configuration for the project-scoped MCP processes."""

import ipaddress
import os
from pathlib import Path
import re
import shutil
import socket
from urllib.parse import parse_qsl, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parents[1]
POLICY_BLOCKED = "[RESEARCH_POLICY_BLOCKED]"
SERVERS = {
    "fetch": {
        "module": "mcp_server_fetch",
        "tools": frozenset({"fetch"}),
    },
    "arxiv": {
        "module": "arxiv_mcp_server",
        "tools": frozenset({
            "search_papers", "get_abstract", "download_paper", "list_papers",
            "read_paper", "get_paper_outline", "read_paper_section",
            "search_paper_text", "export_citations",
        }),
    },
    "context7": {
        "url": "https://mcp.context7.com/mcp",
        "tools": frozenset({"resolve-library-id", "query-docs"}),
    },
    "firecrawl": {
        "url": "https://mcp.firecrawl.dev/v2/mcp",
        "tools": frozenset({"firecrawl_search", "firecrawl_scrape", "firecrawl_parse"}),
    },
}
LOCAL_SERVERS = tuple(name for name, definition in SERVERS.items() if "module" in definition)
ARXIV_ID = re.compile(r"(?:\d{4}\.\d{4,5}|[A-Za-z][A-Za-z.-]*/\d{7})(?:v[1-9]\d*)?")
ARGUMENT_LIMITS = {
    "start": (0, 10_000_000),
    "start_index": (0, 10_000_000),
    "max_length": (1, 60_000),
    "max_chars": (1, 60_000),
    "max_results": (1, 20),
    "max_sections": (1, 50),
    "max_passages": (1, 10),
    "passage_chars": (1, 4_000),
}


def isolated_environment(root=ROOT):
    home = root / ".research" / "home"
    home.mkdir(parents=True, exist_ok=True, mode=0o700)
    paths = [str(root / ".venv" / "bin")]
    node = shutil.which("node")
    if node:
        paths.append(str(Path(node).parent))
    paths.extend(os.defpath.split(os.pathsep))
    return {
        "HOME": str(home),
        "PATH": os.pathsep.join(dict.fromkeys(paths)),
        "LANG": "C.UTF-8",
        "PYTHONUNBUFFERED": "1",
        "PYTHONUTF8": "1",
        "REQUEST_TIMEOUT": "45",
        "MAX_RESULTS": "20",
    }


def upstream_args(server):
    if server not in LOCAL_SERVERS:
        raise ValueError("This server uses a remote HTTP transport")
    args = ["-m", SERVERS[server]["module"]]
    if server == "arxiv":
        args.extend(["--storage-path", str(ROOT / ".research" / "arxiv")])
    return args


def validate_public_url(url):
    """Screen the initial URL; this is not a replacement for network isolation."""
    parsed = urlsplit(url)
    host = parsed.hostname
    if parsed.scheme not in {"http", "https"} or not host:
        raise ValueError("Only public HTTP(S) URLs are permitted")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("Credential-bearing URLs are not permitted")
    if parsed.port not in {None, 80, 443}:
        raise ValueError("Only standard public web ports are permitted")
    if host.lower().rstrip(".").endswith(("localhost", ".local", ".internal")):
        raise ValueError("Local and internal hosts are not permitted")
    if any(key.lower() in {"api_key", "apikey", "access_token", "token", "password"}
           for key, _ in parse_qsl(parsed.query)):
        raise ValueError("Do not send credentials in research URLs")
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    addresses = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(item[4][0]).is_global for item in addresses):
        raise ValueError("The URL must resolve exclusively to public addresses")


def validate_call(server, name, arguments):
    if name not in SERVERS[server]["tools"]:
        raise ValueError("This capability is not enabled in the research profile")
    if not isinstance(arguments, dict):
        raise ValueError("Tool arguments must be an object")
    for argument, (minimum, maximum) in ARGUMENT_LIMITS.items():
        if argument in arguments:
            value = arguments[argument]
            if type(value) is not int or not minimum <= value <= maximum:
                raise ValueError(f"{argument} must be an integer from {minimum} to {maximum}")
    if server == "fetch":
        validate_public_url(arguments.get("url", ""))
    if server == "firecrawl":
        if name == "firecrawl_parse":
            raise ValueError("File uploads and Parse are not enabled in the local public-research bridge")
        if name == "firecrawl_scrape":
            if set(arguments) - {"url", "formats", "onlyMainContent"}:
                raise ValueError("Use basic public scraping without actions, headers or proxy overrides")
            if not isinstance(arguments.get("url"), str):
                raise ValueError("Use a public HTTP(S) URL")
            validate_public_url(arguments["url"])
            formats = arguments.get("formats", ["markdown"])
            if (not isinstance(formats, list) or not 1 <= len(formats) <= 2
                    or any(value not in ("markdown", "links") for value in formats)):
                raise ValueError("Request only markdown or links in the public-research bridge")
            if "onlyMainContent" in arguments and type(arguments["onlyMainContent"]) is not bool:
                raise ValueError("onlyMainContent must be a boolean")
        else:
            if set(arguments) - {"query", "limit"}:
                raise ValueError("Use a public text query and a bounded result limit")
            query = arguments.get("query")
            if not isinstance(query, str) or not query.strip() or len(query) > 4000:
                raise ValueError("Use a nonempty public query of at most 4000 characters")
            limit = arguments.get("limit")
            if type(limit) is not int or not 1 <= limit <= 5:
                raise ValueError("Specify an explicit limit from 1 to 5 search results")
    if server == "arxiv":
        if arguments.get("return_full_text", False) is not False:
            raise ValueError("Read papers in bounded chunks using start and max_chars")
        paper_ids = arguments.get("paper_ids", [])
        if not isinstance(paper_ids, list) or len(paper_ids) > 20:
            raise ValueError("Request at most 20 paper IDs")
        if "paper_id" in arguments:
            paper_ids = [*paper_ids, arguments["paper_id"]]
        if any(not isinstance(value, str) or ARXIV_ID.fullmatch(value) is None for value in paper_ids):
            raise ValueError("Use plain arXiv IDs, such as 1706.03762, not paths or URLs")
        if "query" in arguments:
            query = arguments["query"]
            if not isinstance(query, str) or len(query) > 4000:
                raise ValueError("Use a text query of at most 4000 characters")
