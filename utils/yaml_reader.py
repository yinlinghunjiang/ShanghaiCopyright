import yaml

from libs.models import AuthModel

from contextvars import ContextVar


class Config:
    def __init__(self, config_path: str):
        with open(config_path, "r", encoding="utf-8") as f:
            config_content = yaml.safe_load(f.read())["auth"]
        self.auth = AuthModel(**config_content)


def init_config(config_path: str) -> Config:
    _new = Config(config_path)
    config.set(_new)
    return _new


config = ContextVar("config")
