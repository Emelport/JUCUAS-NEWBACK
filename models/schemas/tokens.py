from pydantic import BaseModel
from datetime import datetime
from settings import SECRET_KEY


class TokenBase(BaseModel):
    user_id: int
    token: str
    created_at: datetime
    expired: bool


class TokenCreate(TokenBase):
    pass


class TokenData(BaseModel):
    username: str

    class Config:
        from_attributes  = True


class Token(TokenBase):
    id: int

    class Config:
        from_attributes  = True


def is_expired(cooldown, created_at):
    now = datetime.now()
    time_difference = now - created_at
    return time_difference.total_seconds() >= cooldown


def check_token(input_token, cooldown, created_at):
    if not is_expired(cooldown, created_at):
        if input_token == SECRET_KEY:
            return "Valid"
        else:
            return "Invalid"
    else:
        return "Expired"
