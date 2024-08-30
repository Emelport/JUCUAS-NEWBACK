from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str
    gender: str
    phone: str

class User(UserBase):
    id: int
    first_name: str
    last_name: str
    gender: str
    phone: str
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


class LoginData(BaseModel):
        username: str
        password: str
