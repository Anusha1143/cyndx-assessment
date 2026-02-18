def web_search_tool(query: str):
    return {
        "tool_name": "web_search",
        "input": {"query": query},
        "output_summary": "Found 12 relevant results..."
    }
