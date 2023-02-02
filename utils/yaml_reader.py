"""
    @Filename: yaml_reader.py
    @Author: Nullqwertyuiop, Little_linnian, Silverowo
    @Time: 2023/1/24
"""

# pylint: disable=too-few-public-methods, import-error

from contextvars import ContextVar

import yaml

from libs.models import AuthModel


class Config:
    """
    The class of read config file
    """

    def __init__(self, config_path: str):
        """
        Open yaml file.

        Args:
            config-path (str): The path of yaml config file
        """
        with open(config_path, "r", encoding="utf-8") as cfg:
            config_content = yaml.safe_load(cfg.read())
        self.auth = AuthModel(**config_content)


def init_config(config_path: str) -> Config:
    """
    Read yaml file, return a object

    Args:
        config-path (str): The path of yaml config file
    """
    _new = Config(config_path)
    config.set(_new)
    return _new


config = ContextVar("config")
