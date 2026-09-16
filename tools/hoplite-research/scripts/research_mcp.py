"""Expose only the audited subset of the installed MCP servers."""

import argparse
import sys

import anyio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import CallToolResult, TextContent

from mcp_runtime import ARGUMENT_LIMITS, LOCAL_SERVERS, POLICY_BLOCKED, ROOT, SERVERS, isolated_environment, upstream_args, validate_call
from prepare_readability import verify_ready


async def guarded_call(client, name, tool_name, arguments):
    with anyio.fail_after(90):
        try:
            await anyio.to_thread.run_sync(
                validate_call, name, tool_name, arguments, abandon_on_cancel=True
            )
        except ValueError as exc:
            return CallToolResult(isError=True, content=[
                TextContent(type="text", text=f"{POLICY_BLOCKED} {exc}")
            ])
        return await client.call_tool(tool_name, arguments)


async def serve(name):
    if name == "fetch":
        verify_ready()
    upstream = StdioServerParameters(
        command=sys.executable, args=upstream_args(name),
        cwd=str(ROOT), env=isolated_environment(),
    )
    async with stdio_client(upstream) as (reader, writer):
        async with ClientSession(reader, writer) as client:
            with anyio.fail_after(30):
                await client.initialize()
                catalog = await client.list_tools()
            tools = [tool for tool in catalog.tools if tool.name in SERVERS[name]["tools"]]
            for tool in tools:
                properties = tool.inputSchema.get("properties", {})
                for argument, (minimum, maximum) in ARGUMENT_LIMITS.items():
                    if argument in properties:
                        properties[argument].update(
                            minimum=max(minimum, properties[argument].get("minimum", minimum)),
                            maximum=min(maximum, properties[argument].get("maximum", maximum)),
                        )
                if "return_full_text" in properties:
                    properties["return_full_text"].update(
                        const=False, description="Read in bounded chunks; full-text opt-out is disabled."
                    )
                if "paper_id" in properties:
                    properties["paper_id"]["description"] = "Plain arXiv ID, such as 1706.03762; no paths or URLs."
                if "paper_ids" in properties:
                    properties["paper_ids"]["maxItems"] = 20
            missing = SERVERS[name]["tools"] - {tool.name for tool in tools}
            if missing:
                raise RuntimeError(f"Installed server is missing expected tools: {sorted(missing)}")
            server = Server(f"research-{name}", version="0.1.0")

            @server.list_tools()
            async def list_tools():
                return tools

            @server.call_tool()
            async def call_tool(tool_name, arguments):
                return await guarded_call(client, name, tool_name, arguments)

            async with stdio_server() as (incoming, outgoing):
                await server.run(incoming, outgoing, server.create_initialization_options())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("server", choices=LOCAL_SERVERS)
    anyio.run(serve, parser.parse_args().server)
