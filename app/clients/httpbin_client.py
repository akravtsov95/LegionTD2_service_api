import httpx

class HttpBinClient:
    async def get_ip(self, client: httpx.AsyncClient) -> dict:
        resp = await client.get("https://httpbin.org/ip")
        resp.raise_for_status()
        return resp.json()