from pydantic import BaseModel
from typing import Optional
from models.choices import UniversityRegion as Region  # Importa el Enum necesario desde models.choices si es necesario

# Modelo Pydantic para la creación de revisores
class ReviewerCreate(BaseModel):
    user_id: Optional[int]
    first_name: str
    last_name: str
    user_name: str
    region: Optional[Region]  # Asegúrate de importar 'Region' desde models.choices si es necesario
    global_reviewer: Optional[bool]
    origin_university_id: Optional[int]
    origin_highschool_id: Optional[int]
    origin_organizational_unit_id: Optional[int]
    reviewer_permission: Optional[str]
    email: Optional[str]
    is_active: Optional[bool]
    status: Optional[bool]

# Modelo Pydantic para la actualización de revisores
class ReviewerUpdate(BaseModel):
    user_id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    user_name: Optional[str]
    region: Optional[Region]  # Asegúrate de importar 'Region' desde models.choices si es necesario
    global_reviewer: Optional[bool]
    origin_university_id: Optional[int]
    origin_highschool_id: Optional[int]
    origin_organizational_unit_id: Optional[int]
    reviewer_permission: Optional[str]
    email: Optional[str]
    is_active: Optional[bool]
    status: Optional[bool]

# Modelo Pydantic para la lectura de revisores (con ID y relaciones resueltas)
class Reviewer(BaseModel):
    id: int
    user_id: Optional[int]
    first_name: str
    last_name: str
    user_name: str
    region: Optional[Region]  # Asegúrate de importar 'Region' desde models.choices si es necesario
    global_reviewer: bool
    origin_university_id: Optional[int]
    origin_highschool_id: Optional[int]
    origin_organizational_unit_id: Optional[int]
    reviewer_permission: Optional[str]
    email: Optional[str]
    is_active: bool
    status: bool

    class Config:
        from_attributes = True
