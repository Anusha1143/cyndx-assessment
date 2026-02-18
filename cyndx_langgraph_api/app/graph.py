import time
import uuid
from datetime import datetime
from .nodes import run_agent_logic


def execute_graph(session_id: str, content: str):
    start = time.time()

    response_text, tool_calls, usage = run_agent_logic(content)

    latency = int((time.time() - start) * 1000)

    return {
        "message_id": f"msg_{uuid.uuid4().hex[:12]}",
        "session_id": session_id,
        "role": "assistant",
        "content": response_text,
        "tool_calls": tool_calls,
        "usage": usage,
        "latency_ms": latency,
        "created_at": datetime.utcnow()
    }
