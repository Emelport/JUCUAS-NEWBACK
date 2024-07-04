from pydantic import BaseModel
from typing import Optional
from models.choices import TypeEvidence  # Asegúrate de importar los enums necesarios desde models.choices

# Modelo Pydantic para el tipo de evidencia
class TypeEvidenceBase(BaseModel):
    name: str
    type: TypeEvidence
    is_active: bool = True
    status: bool = True
    is_optional: bool = False

    class Config:
        orm_mode = True

# Modelo Pydantic para la creación del tipo de evidencia
class TypeEvidenceCreate(TypeEvidenceBase):
    pass

# Modelo Pydantic para la actualización del tipo de evidencia
class TypeEvidenceUpdate(TypeEvidenceBase):
    id: int

# Modelo Pydantic para la respuesta del tipo de evidencia
class TypeEvidence(TypeEvidenceBase):
    id: int

    class Config:
        orm_mode = True
