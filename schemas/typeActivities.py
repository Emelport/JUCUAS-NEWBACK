from pydantic import BaseModel, conlist
from typing import List, Optional
from models.choices import TypeEvidence  # Asegúrate de importar los enums necesarios desde models.choices

# Modelo Pydantic para el tipo de actividad
class TypeActivityBase(BaseModel):
    name: str
    title: Optional[str]
    max_copresenter: Optional[str]
    is_active: bool = True
    status: bool = True
    type_evidence_ids: Optional[List[int]] = []

    class Config:
        from_attributes = True

# Modelo Pydantic para la creación del tipo de actividad
class TypeActivityCreate(TypeActivityBase):
    pass

# Modelo Pydantic para la actualización del tipo de actividad
class TypeActivityUpdate(TypeActivityBase):
    id: int

# Modelo Pydantic para la respuesta del tipo de actividad
class TypeActivity(TypeActivityBase):
    id: int
    type_evidences: Optional[List[TypeEvidence]] = []

    class Config:
        from_attributes = True
