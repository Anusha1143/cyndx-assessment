from fastapi import HTTPException
import uuid


def api_error(code: str, message: str, status_code: int):
    return HTTPException(
        status_code=status_code,
        detail={
            "error": {
                "code": code,
                "message": message,
                "details": {},
                "request_id": f"req_{uuid.uuid4().hex[:8]}"
            }
        }
    )
