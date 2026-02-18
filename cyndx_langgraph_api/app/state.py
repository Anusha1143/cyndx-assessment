from datetime import datetime, timezone
import uuid

sessions = {}
messages = {}


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def create_session(agent_config):
    session_id = f"sess_{uuid.uuid4().hex[:12]}"

    session = {
        "session_id": session_id,
        "created_at": utc_now(),
        "status": "active",
        "agent_config": agent_config,
    }

    sessions[session_id] = session
    messages[session_id] = []

    return session


def get_session(session_id):
    return sessions.get(session_id)


def delete_session(session_id):
    session = sessions.get(session_id)

    if not session:
        return None

    session["status"] = "terminated"
    session["deleted_at"] = utc_now()

    return session


def add_message(session_id, message):
    messages[session_id].append(message)


def get_history(session_id):
    return messages.get(session_id, [])
