from pydantic import BaseModel
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str
    created_at: datetime
    expires_at: datetime

class TokenCreate(BaseModel):
    username: str
    password: str
