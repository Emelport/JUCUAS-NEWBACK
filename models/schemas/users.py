from pydantic import BaseModel, EmailStr
from typing import Optional
from models.choices import GenderEnum as Gender  # Importa el Enum de choices si es necesario


# Modelo Pydantic para la creación de usuarios
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Gender]  # Asegúrate de importar 'Gender' desde models.choices si es necesario
    phone: Optional[str]


# Modelo Pydantic para la actualización de usuarios
class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Gender]  # Asegúrate de importar 'Gender' desde models.choices si es necesario
    phone: Optional[str]


# Modelo Pydantic para la lectura de usuarios (con ID)
class User(UserCreate):
    id: int

    class Config:
        from_attributes = True
