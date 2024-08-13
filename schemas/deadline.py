from pydantic import BaseModel
from typing import Optional
from datetime import date

# Modelo Pydantic para leer datos de Deadline
class Deadline(BaseModel):
    id: int
    name_edition: str
    date_edition: str
    date_to_upload_activities: Optional[date]
    date_to_upload_evidence: Optional[date]
    date_to_validate_evidence: Optional[date]
    date_edition_start: Optional[date]
    end_date_of_the_edition: Optional[date]
    is_active: bool
    status: bool
    file: Optional[str]
    file_name: Optional[str]

    class Config:
        from_attributes = True

# Modelo Pydantic para crear un nuevo Deadline
class DeadlineCreate(BaseModel):
    name_edition: str
    date_edition: str
    date_to_upload_activities: Optional[date]
    date_to_upload_evidence: Optional[date]
    date_to_validate_evidence: Optional[date]
    date_edition_start: Optional[date]
    end_date_of_the_edition: Optional[date]
    is_active: bool = True
    status: bool = True
    file: Optional[str] = None
    file_name: Optional[str] = None

# Modelo Pydantic para actualizar un Deadline existente
class DeadlineUpdate(BaseModel):
    name_edition: Optional[str]
    date_edition: Optional[str]
    date_to_upload_activities: Optional[date]
    date_to_upload_evidence: Optional[date]
    date_to_validate_evidence: Optional[date]
    date_edition_start: Optional[date]
    end_date_of_the_edition: Optional[date]
    is_active: Optional[bool]
    status: Optional[bool]
    file: Optional[str]
    file_name: Optional[str]

# Modelo Pydantic para la carga de archivos
class DeadlineUploadFile(BaseModel):
    id: int
    file_name: str
    file: str
