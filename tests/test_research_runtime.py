from pathlib import Path
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "tools/hoplite-research/scripts"
sys.path.insert(0, str(SCRIPTS))

from mcp_runtime import isolated_environment, validate_call, validate_public_url


def address(ip="93.184.215.14"):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (ip, 443))]


class PublicURLTests(unittest.TestCase):
    def test_public_https(self):
        with patch("mcp_runtime.socket.getaddrinfo", return_value=address()):
            validate_public_url("https://example.com/research?topic=business")

    def test_http_uses_http_port(self):
        with patch("mcp_runtime.socket.getaddrinfo", return_value=address()) as resolve:
            validate_public_url("http://example.com/research")
        resolve.assert_called_once_with("example.com", 80, type=socket.SOCK_STREAM)

    def test_rejects_nonpublic_and_credential_urls(self):
        for url in ["file:///etc/passwd", "ftp://example.com", "https://user:pass@example.com",
                    "https://localhost", "http://service.internal", "https://box.local",
                    "https://example.com:8443", "https://example.com?api_key=synthetic",
                    "https://example.com?access_token=synthetic"]:
            with self.subTest(url=url), patch("mcp_runtime.socket.getaddrinfo") as resolve:
                with self.assertRaises(ValueError):
                    validate_public_url(url)
                resolve.assert_not_called()

    def test_rejects_private_or_mixed_dns_answers(self):
        for addresses in [[], address("127.0.0.1"), address("10.0.0.1"),
                          address("169.254.169.254"), address("192.168.0.1"),
                          address("::1"), address() + address("10.0.0.1")]:
            with self.subTest(addresses=addresses):
                with patch("mcp_runtime.socket.getaddrinfo", return_value=addresses):
                    with self.assertRaises(ValueError):
                        validate_public_url("https://example.com")


class ToolPolicyTests(unittest.TestCase):
    def test_limits_reject_bools_floats_and_unbounded_numbers(self):
        for value in [True, 0, -1, 21, "2", 2.5]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_call("arxiv", "search_papers", {"query": "AI", "max_results": value})

    def test_arxiv_ids_and_bounded_reads(self):
        for paper_id in ["1706.03762", "1706.03762v2", "cs/9901001"]:
            validate_call("arxiv", "get_abstract", {"paper_id": paper_id})
        for arguments in [{"paper_id": "../../etc/passwd"}, {"paper_id": "https://arxiv.org/abs/1706.03762"},
                          {"paper_ids": ["1706.03762"] * 21}, {"return_full_text": True},
                          {"max_chars": 60001}]:
            with self.subTest(arguments=arguments), self.assertRaises(ValueError):
                validate_call("arxiv", "read_paper", arguments)

    def test_firecrawl_only_bounded_public_search(self):
        validate_call("firecrawl", "firecrawl_search", {"query": "public market research", "limit": 3})
        for args in [{"query": "AI"}, {"query": "AI", "limit": 6}, {"query": "", "limit": 1},
                     {"query": "x" * 4001, "limit": 1}, {"query": "AI", "limit": 1, "enterprise": ["anon"]}]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                validate_call("firecrawl", "firecrawl_search", args)

    def test_firecrawl_disallows_uploads_actions_and_overrides(self):
        with self.assertRaises(ValueError):
            validate_call("firecrawl", "firecrawl_parse", {"filePath": "anything.pdf"})
        with patch("mcp_runtime.validate_public_url"):
            validate_call("firecrawl", "firecrawl_scrape", {"url": "https://example.com", "formats": ["markdown"]})
            for extra in [{"proxy": "auto"}, {"headers": {"X-Test": "synthetic"}},
                          {"actions": []}, {"formats": ["html"]}, {"onlyMainContent": "true"}]:
                with self.subTest(extra=extra), self.assertRaises(ValueError):
                    validate_call("firecrawl", "firecrawl_scrape", {"url": "https://example.com", **extra})

    def test_unknown_tool_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_call("fetch", "execute_code", {})

    def test_environment_does_not_forward_secrets(self):
        with tempfile.TemporaryDirectory() as folder, patch.dict("os.environ", {
            "GITHUB_TOKEN": "synthetic", "OPENAI_API_KEY": "synthetic", "HTTP_PROXY": "synthetic",
        }):
            env = isolated_environment(Path(folder))
            self.assertNotIn("GITHUB_TOKEN", env)
            self.assertNotIn("OPENAI_API_KEY", env)
            self.assertNotIn("HTTP_PROXY", env)
            self.assertEqual(env["HOME"], str(Path(folder) / ".research/home"))


if __name__ == "__main__":
    unittest.main()
