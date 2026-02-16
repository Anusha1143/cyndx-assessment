import logging
import sys
import json
import time

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "severity": record.levelname,
            "message": record.getMessage(),
            "timestamp": time.time(),
            "request_id": getattr(record, "request_id", None),
            "session_id": getattr(record, "session_id", None),
            "endpoint": getattr(record, "endpoint", None),
            "status_code": getattr(record, "status_code", None),
            "latency_ms": getattr(record, "latency_ms", None),
        })

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)
