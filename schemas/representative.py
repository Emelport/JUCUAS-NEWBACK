from pydantic import BaseModel
from typing import Optional

# Modelo Pydantic para la creación de representantes
class RepresentativeCreate(BaseModel):
    user_id: Optional[int]
    first_name: str
    last_name: str
    user_name: str
    origin_university_id: Optional[int]
    origin_organizational_unit_id: Optional[int]
    email: Optional[str]
    is_active: Optional[bool]
    status: Optional[bool]

# Modelo Pydantic para la actualización de representantes
class RepresentativeUpdate(BaseModel):
    user_id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    user_name: Optional[str]
    origin_university_id: Optional[int]
    origin_organizational_unit_id: Optional[int]
    email: Optional[str]
    is_active: Optional[bool]
    status: Optional[bool]

# Modelo Pydantic para la lectura de representantes (con ID y relaciones resueltas)
class Representative(BaseModel):
    id: int
    user_id: Optional[int]
    first_name: str
    last_name: str
    user_name: str
    origin_university_id: Optional[int]
    origin_organizational_unit_id: Optional[int]
    email: Optional[str]
    is_active: bool
    status: bool

    class Config:
        orm_mode = True
