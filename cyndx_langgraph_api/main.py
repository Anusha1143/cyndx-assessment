from fastapi import FastAPI
from app.routes import router
from core.middleware import add_middlewares

app = FastAPI(title="Cyndx LangGraph API")

add_middlewares(app)
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Cyndx LangGraph API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}
