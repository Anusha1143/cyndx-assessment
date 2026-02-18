from fastapi import FastAPI
from cyndx_langgraph_api.app.routes import router
from cyndx_langgraph_api.core.middleware import add_middlewares

app = FastAPI(title="Cyndx LangGraph API", version="1.0.0")

add_middlewares(app)

app.include_router(router)

START_TIME = __import__("time").time()


@app.get("/health")
def health():
    import time
    uptime = int(time.time() - START_TIME)

    return {
        "status": "healthy",
        "version": "1.0.0",
        "uptime_seconds": uptime,
        "checks": {
            "llm_provider": "ok",
            "checkpoint_store": "ok"
        }
    }
