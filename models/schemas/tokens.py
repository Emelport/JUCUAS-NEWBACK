from pydantic import BaseModel
from datetime import datetime, timedelta
import secrets

class TokenBase(BaseModel):
    user_id: int
    token: str
    created_at: datetime
    expired: bool

class TokenCreate(TokenBase):
    pass

class Token(TokenBase):
    id: int

    class Config:
        orm_mode = True

def generate_token():
    return ''.join(str(secrets.randbelow(10)) for _ in range(6))

def is_expired(cooldown, created_at):
    now = datetime.now()
    time_difference = now - created_at
    return time_difference.total_seconds() >= cooldown

def check_token(token, cooldown, created_at):
    if not is_expired(cooldown, created_at):
        if token == token:
            return "Valid"
        else:
            return "Invalid"
    else:
        return "Expired"
