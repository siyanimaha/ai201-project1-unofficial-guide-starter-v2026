from mcp.server.fastmcp import FastMCP
from store import search

mcp = FastMCP("Campus Guide MCP")


@mcp.tool()
def search_listings(
    question: str,
    top_k: int = 5,
    corpus: str | None = None,
) -> list[dict]:
    """Search the indexed campus guide listings for information relevant to a question."""
    results = search(
        question=question,
        top_k=top_k,
        corpus=corpus,
    )

    return [
        {
            "text": result.text,
            "source": result.source,
            "label": result.label,
            "distance": result.distance,
            "produced_by": result.produced_by,
        }
        for result in results
    ]


if __name__ == "__main__":
    mcp.run()
