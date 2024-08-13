from pydantic import BaseModel
from typing import Optional
from models.choices import EducationalLevel as UniversityType, UniversityRegion as Region  # Asegúrate de importar los Enums necesarios desde models.choices si es necesario

# Modelo Pydantic para la creación de universidades
class UniversityCreate(BaseModel):
    name: str
    acronym: str
    key_code: str
    type: Optional[UniversityType]  # Asegúrate de importar 'UniversityType' desde models.choices si es necesario
    region: Optional[Region]  # Asegúrate de importar 'Region' desde models.choices si es necesario
    municipality: str
    locality: str
    email: Optional[str]
    phone: Optional[str]

# Modelo Pydantic para la actualización de universidades
class UniversityUpdate(BaseModel):
    name: Optional[str]
    acronym: Optional[str]
    key_code: Optional[str]
    type: Optional[UniversityType]  # Asegúrate de importar 'UniversityType' desde models.choices si es necesario
    region: Optional[Region]  # Asegúrate de importar 'Region' desde models.choices si es necesario
    municipality: Optional[str]
    locality: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    is_active: Optional[bool]
    status: Optional[bool]

# Modelo Pydantic para la lectura de universidades (con ID)
class University(BaseModel):
    id: int
    name: str
    acronym: str
    key_code: str
    type: Optional[UniversityType]
    region: Optional[Region]
    municipality: str
    locality: str
    email: Optional[str]
    phone: Optional[str]
    is_active: bool
    status: bool

    class Config:
        from_attributes = True
