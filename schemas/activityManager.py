from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from models.choices import Gender, AcademicDegree

# Modelo Pydantic para el responsable de actividad
class ActivityManager(BaseModel):
    id: int
    user_id: Optional[int]
    first_name: str
    last_name: str
    gender: Optional[Gender]
    academic_degree: Optional[AcademicDegree]
    email: Optional[str]
    birth_date: Optional[datetime]
    is_active: bool
    status: bool

    class Config:
        orm_mode = True

class ActivityManagerCreate(BaseModel):
    user_id: Optional[int]
    first_name: str
    last_name: str

class ActivityManagerUpdate(BaseModel):
    user_id: Optional[int]
    first_name: str
    last_name: str
