from pydantic import BaseModel
from typing import Optional
from datetime import date

# Modelo Pydantic para fechas límite
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
        orm_mode = True
