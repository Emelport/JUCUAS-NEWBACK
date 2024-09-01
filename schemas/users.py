from typing import Optional, List

from pydantic import BaseModel, EmailStr

from schemas.groups import GroupOut


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
    groups: Optional[List[str]]  # Lista de nombres de grupos

    class Config:
        from_attributes = True



class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    groups: Optional[List[str]] = None  # Lista de nombres de grupos


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class LoginData(BaseModel):
        username: str
        password: str


class ChangePassword(BaseModel):
    actual_password: str
    passwd1: str
    passwd2: str



class UserResponse(BaseModel):
    username: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    phone: Optional[str]
    groups: Optional[List[str]]  # Lista de nombres de grupos

    class Config:
        from_attributes = True

class UserOut(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    gender: str
    phone: str
    is_active: bool
    is_superuser: bool
    groups: List[GroupOut]

    class Config:
        from_attributes = True
