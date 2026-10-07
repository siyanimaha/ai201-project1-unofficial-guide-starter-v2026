import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def search_via_mcp_async(question, top_k=3, corpus=None):
    from store import Result

    server = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"],
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            arguments = {
                "question": question,
                "top_k": top_k,
            }

            if corpus is not None:
                arguments["corpus"] = corpus

            response = await session.call_tool(
                "search_listings",
                arguments=arguments,
            )

            rows = response.structuredContent["result"]

            return [
                Result(
                    text=row["text"],
                    source=row["source"],
                    label=row["label"],
                    distance=row["distance"],
                    produced_by=row["produced_by"],
                )
                for row in rows
            ]


def search_via_mcp(question, top_k=3, corpus=None):
    return asyncio.run(
        search_via_mcp_async(
            question=question,
            top_k=top_k,
            corpus=corpus,
        )
    )
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
