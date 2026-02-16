from fastapi import APIRouter, HTTPException
from cyndx_langgraph_api.app.graph import run_graph
from cyndx_langgraph_api.app.state import sessions

router = APIRouter()

@router.post("/sessions")
def create_session(user_id: str):
    sessions[user_id] = []
    return {"session_id": user_id}

@router.post("/sessions/{session_id}/messages")
def send_message(session_id: str, message: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    response = run_graph(message)
    sessions[session_id].append(message)

    return {"response": response}

@router.get("/health")
def health():
    return {"status": "ok"}
