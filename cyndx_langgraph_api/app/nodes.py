from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from .tools import web_search_tool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


def run_agent_logic(content: str):
    tool_calls = []

    # Simple routing example
    if "acquired" in content.lower():
        tool_result = web_search_tool(content)
        tool_calls.append(tool_result)

    response = llm.invoke([HumanMessage(content=content)])

    usage = {
        "prompt_tokens": response.response_metadata["token_usage"]["prompt_tokens"],
        "completion_tokens": response.response_metadata["token_usage"]["completion_tokens"],
        "total_tokens": response.response_metadata["token_usage"]["total_tokens"],
        "llm_calls": 1
    }

    return response.content, tool_calls, usage
