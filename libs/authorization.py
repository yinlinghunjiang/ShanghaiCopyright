from utils import sessions
from utils import Config
from libs.exceptions import TokenInvalid, ResponseEmpty
from libs.models import AccessToken

from pydantic import ValidationError


URL: str = (
    "https://shbqdj.cn/MobileApi/Authorization/OAuth2/access_token"
    "?grant_type={grant_type}&client_id={cid}&client_secret={client_secret}"
)

HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
    "Safari/537.36 Edg/108.0.1462.76",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json; charset=utf-8",
}


async def get_token(cfg: Config, session: str = "universal") -> AccessToken:
    client = await sessions.get(session)

    async with client.get(
        URL.format(
            grant_type=cfg.auth.grant_type,
            cid=cfg.auth.client_id,
            client_secret=cfg.auth.client_secret,
        ),
        headers=HEADERS,
    ) as resp:
        resp.raise_for_status()
        try:
            return AccessToken.parse_raw(await resp.text())
        except ValidationError as e:
            raise TokenInvalid from e


# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(get_token())
