from fastapi import APIRouter, Query, Request
from pydantic import BaseModel, Field

from app.clients.httpbin_client import HttpBinClient

router = APIRouter(prefix="/v1", tags=["v1"])
httpbin_client = HttpBinClient()

class PlayerResolveResponse(BaseModel):
    player_id: str = Field(..., description="Player ID")
    nickname: str = Field(..., description="Requested nickname")


@router.get("/players/resolve", response_model=PlayerResolveResponse)
async def resolve_player(nickname: str = Query(..., min_length=2, max_length=32)) -> PlayerResolveResponse:
    return PlayerResolveResponse(player_id=f"stub-{nickname.lower()}", nickname=nickname)


@router.get("/debug/ip")
async def debug_ip(request: Request):
    data = await httpbin_client.get_ip(request.app.state.http)
    return {"upstream": data}