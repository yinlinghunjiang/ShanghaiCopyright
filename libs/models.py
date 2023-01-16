from pydantic import BaseModel


class AuthModel(BaseModel):

    grant_type: str

    client_id: str

    client_secret: str


class AccessToken(BaseModel):

    access_token: str

    token_type: str

    expires_in: int

    refresh_token: str

    scope: str

    system_id: int

    certificate_id: int

    id_token: str
