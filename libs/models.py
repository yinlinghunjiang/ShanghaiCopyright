"""
    @Filename: models.py
    @Author: Silverowo, Nullqwertyuiop
    @Time: 2023/1/24
"""

# pylint: disable=too-few-public-methods, no-name-in-module

from pydantic import BaseModel


class AuthModel(BaseModel):
    """
    Model for auth

    Args:
        BaseModel (BaseModel): Class from pydantic
    """
    grant_type: str

    client_id: str

    client_secret: str


class AccessToken(BaseModel):
    """
    Model for AccessToken

    Args:
        BaseModel (BaseModel): Class from pydantic
    """
    access_token: str

    token_type: str

    expires_in: int

    refresh_token: str

    scope: str

    system_id: int

    certificate_id: int

    id_token: str
