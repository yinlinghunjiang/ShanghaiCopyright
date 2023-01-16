import asyncio
import json
from utils import init_config, config, sessions
from libs.authorization import get_token

init_config("./config/configs.yml")
# cfg: Config = config.get()


async def get_elements(**_kwargs: map) -> None:
    data = {
        "DataSource": {"CommandText": "select name from sysobjects where xtype='U'"}
    }
    token = await get_token(config.get())
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0"
        "Safari/537.36 Edg/108.0.1462.76",
        "accept": "application/json",
        "Authorization": token.id_token,
        "Content-Type": "application/json-patch+json",
    }
    url = "https://shbqdj.cn/MobileApi/WorkFlow/FlowProcess/ExecSql"
    session = await sessions.get()
    async with session.post(url, data=json.dumps(data), headers=headers) as res:
        raw = json.loads(await res.text())
    for i in range(len(raw)):
        data = {
            "DataSource": {
                "CommandText": f"select top 1 * from {raw[i]['name']} order by InputTime DESC"
            }
        }
        async with session.post(url, data=json.dumps(data), headers=headers) as r:
            if r.status == 200 and await r.text() != "[]":
                with open("./output/" + raw[i]["name"] + ".json", "w", encoding="UTF-8") as f:
                    f.write(await r.text())


asyncio.run(get_elements())
