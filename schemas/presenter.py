from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Modelo Pydantic para la creación de presentadores
class PresenterCreate(BaseModel):
    user_id: Optional[int]
    first_name: str
    last_name: str
    user_name: str
    gender: Optional[str]
    curp: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    academic_degree: Optional[str]
    origin_university_id: Optional[int]
    origin_organizational_unit_id: Optional[int]
    if_belong_to_school: Optional[bool]
    position_institution: Optional[str]
    birth_date: Optional[datetime]
    created_by_id: Optional[int]
    is_active: Optional[bool]
    status: Optional[bool]

# Modelo Pydantic para la actualización de presentadores
class PresenterUpdate(BaseModel):
    user_id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    user_name: Optional[str]
    gender: Optional[str]
    curp: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    academic_degree: Optional[str]
    origin_university_id: Optional[int]
    origin_organizational_unit_id: Optional[int]
    if_belong_to_school: Optional[bool]
    position_institution: Optional[str]
    birth_date: Optional[datetime]
    created_by_id: Optional[int]
    is_active: Optional[bool]
    status: Optional[bool]

    # Modelo Pydantic para la lectura de presentadores (con ID y relaciones resueltas)
class Presenter(BaseModel):
    id: int
    user_id: Optional[int]
    first_name: str
    last_name: str
    user_name: str
    gender: Optional[str]
    curp: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    academic_degree: Optional[str]
    origin_university_id: Optional[int]
    origin_organizational_unit_id: Optional[int]
    if_belong_to_school: bool
    position_institution: str
    birth_date: Optional[datetime]
    created_by_id: Optional[int]
    is_active: bool
    status: bool

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

