import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"],
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()

            print("Available MCP tools:")
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")

            print("\nTesting search_listings...")
            result = await session.call_tool(
                "search_listings",
                arguments={
                    "question": "Where can I study on campus?",
                    "top_k": 3,
                },
            )

            print(result)


if __name__ == "__main__":
    asyncio.run(main())
