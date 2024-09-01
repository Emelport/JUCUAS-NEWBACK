from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Token(BaseModel):
    access_token: str
    refresh_token: Optional[str]  # Asegúrate de que esto esté presente
    token_type: str
    created_at: datetime
    expires_at: datetime
    expires_in: int


class TokenCreate(BaseModel):
    username: str
    password: str
