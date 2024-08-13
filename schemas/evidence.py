from pydantic import BaseModel
from typing import Optional
from schemas.users import User  # Asegúrate de importar el modelo Pydantic de User si lo tienes definido

# Modelo Pydantic para Evidence
class Evidence(BaseModel):
    id: int
    name: str
    observation: Optional[str]
    evidence_file: Optional[str]
    evidence_status: str
    created_by: Optional[User]
    status_changed_by: Optional[User]
    type_evidence_id: Optional[int]
    activity_id: Optional[int]

    class Config:
        from_attributes = True
