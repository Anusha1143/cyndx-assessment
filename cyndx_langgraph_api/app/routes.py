from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uuid
from datetime import datetime, timezone

from .state import (
    create_session,
    get_session,
    delete_session,
    add_message,
    get_history
)
from .graph import execute_graph
from cyndx_langgraph_api.core.errors import api_error

router = APIRouter()


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


# ---------------------------
# MODELS
# ---------------------------

class AgentConfig(BaseModel):
    model: str = "gpt-4o-mini"
    temperature: float = 0.7


class CreateSessionRequest(BaseModel):
    agent_config: Optional[AgentConfig] = None


class MessageRequest(BaseModel):
    content: str
    metadata: Optional[Dict[str, Any]] = {}


# ---------------------------
# POST /sessions
# ---------------------------

@router.post("/sessions", status_code=201)
def create_new_session(request: CreateSessionRequest):
    agent_config = request.agent_config.dict() if request.agent_config else AgentConfig().dict()

    session = create_session(agent_config)

    # Return EXACT required structure
    return {
        "session_id": session["session_id"],
        "created_at": session["created_at"],
        "status": session["status"],
        "agent_config": session["agent_config"]
    }


# ---------------------------
# POST /sessions/{id}/messages
# ---------------------------

@router.post("/sessions/{session_id}/messages")
def send_message(session_id: str, request: MessageRequest):

    session = get_session(session_id)

    if not session or session["status"] != "active":
        raise api_error(
            "SESSION_NOT_FOUND",
            f"No active session found with ID '{session_id}'.",
            404
        )

    # Save user message
    user_message = {
        "message_id": f"msg_{uuid.uuid4().hex[:12]}",
        "role": "user",
        "content": request.content,
        "created_at": utc_now()
    }

    add_message(session_id, user_message)

    # Execute graph
    agent_output = execute_graph(session_id, request.content)

    add_message(session_id, agent_output)

    return agent_output


# ---------------------------
# GET /sessions/{id}/history
# ---------------------------

@router.get("/sessions/{session_id}/history")
def get_session_history(session_id: str):

    session = get_session(session_id)

    if not session:
        raise api_error(
            "SESSION_NOT_FOUND",
            f"No session found with ID '{session_id}'.",
            404
        )

    history = get_history(session_id)

    return {
        "session_id": session_id,
        "message_count": len(history),
        "messages": history
    }


# ---------------------------
# DELETE /sessions/{id}
# ---------------------------

@router.delete("/sessions/{session_id}")
def terminate_session(session_id: str):

    session = delete_session(session_id)

    if not session:
        raise api_error(
            "SESSION_NOT_FOUND",
            f"No session found with ID '{session_id}'.",
            404
        )

    # 🔥 RETURN ONLY WHAT SPEC REQUIRES
    return {
        "session_id": session["session_id"],
        "status": session["status"],
        "deleted_at": session["deleted_at"]
    }
