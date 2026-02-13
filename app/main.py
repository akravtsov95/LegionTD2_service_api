from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI
from app.core.settings import settings
from app.api.v1.routes import router as v1_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http = httpx.AsyncClient(timeout=10.0)
    yield
    await app.state.http.aclose()

app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.include_router(v1_router)

@app.get("/health")
def health():
    return {"ok": True, "env": settings.env}