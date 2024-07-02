from pydantic import BaseModel
from typing import Optional
from models.choices import UniversityRegion as Region  # Importa el Enum necesario desde models.choices si es necesario

# Modelo Pydantic para la creación de unidades organizacionales
class OrganizationalUnitCreate(BaseModel):
    name: str
    acronym: str
    key_code: str
    region: Optional[Region]  # Asegúrate de importar 'Region' desde models.choices si es necesario
    municipality: str
    locality: str
    email: Optional[str]
    phone: Optional[str]

# Modelo Pydantic para la actualización de unidades organizacionales
class OrganizationalUnitUpdate(BaseModel):
    name: Optional[str]
    acronym: Optional[str]
    key_code: Optional[str]
    region: Optional[Region]  # Asegúrate de importar 'Region' desde models.choices si es necesario
    municipality: Optional[str]
    locality: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    is_active: Optional[bool]
    status: Optional[bool]

# Modelo Pydantic para la lectura de unidades organizacionales (con ID)
class OrganizationalUnit(OrganizationalUnitCreate):
    id: int
    is_active: bool
    status: bool

    class Config:
        orm_mode = True
