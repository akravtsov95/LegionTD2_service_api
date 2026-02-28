from fastapi import HTTPException
import httpx

class PlayerService:
    async def resolve(self, http: httpx.AsyncClient, nickname: str) -> dict:
        url ="https://httpbin.org/status/200"
        try:
            resp = await http.get(url)
            resp.raise_for_status()
            return {"player_id": f"stub-{nickname.lower()}", "nickname": nickname}
        except httpx.TimeoutException:
            raise HTTPException(status_code=504, detail="Upstream timeout")
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=502, detail=f"Upstream error: {e.response.status_code}")
        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"Upstream request failed: {type(e).__name__}")