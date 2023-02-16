"""
    @Filename: main.py
    @Author: Silverowo, Nullqwertyuiop
    @Time: 2023/1/24
"""

# pylint: disable=consider-using-enumerate

import asyncio
import json
from pathlib import Path
from utils import init_config, config, sessions
from libs.authorization import get_token
from loguru import logger

init_config("./config/configs.yml")
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


async def get_elements() -> None:
    """
    Get datebase elements from ShanghaiCopyright MobileApi
    """
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
        data = {"DataSource": {"CommandText": f"select * from {raw[i]['name']}"}}
        async with session.post(url, data=json.dumps(data), headers=headers) as resp:
            if resp.status == 200:
                logger.info(f"正在下载{raw[i]['name']}")
                with open(
                    OUTPUT_DIR / f"{raw[i]['name']}.json", "w", encoding="UTF-8"
                ) as file:
                    file.write(await resp.text())
                    logger.info(f"正在写入至{raw[i]['name']}.json")

asyncio.run(get_elements())
