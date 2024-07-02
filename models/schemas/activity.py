from pydantic import BaseModel, conlist
from typing import List, Optional
from datetime import datetime
from models.choices import Modality, EducationalLevel, TypeOfPublic, AreaKnowledge, ActivityStatus
from models.schemas import presenter, typeActivities  # Asegúrate de importar los modelos Pydantic necesarios

# Modelo Pydantic para la actividad
class ActivityBase(BaseModel):
    name: str
    description: Optional[str]
    numbers_expected_attendees: Optional[int]
    numbers_total_attendees: Optional[int]
    modality: Optional[Modality]
    edition_id: Optional[int]
    date_activity: Optional[datetime]
    educational_level_to_is_directed: Optional[EducationalLevel]
    type_of_public: Optional[TypeOfPublic]
    area_knowledge: Optional[AreaKnowledge]
    presenter_id: Optional[int]
    co_presenter_ids: Optional[List[int]] = []
    type_id: Optional[int]
    created_by_id: Optional[int]
    certificate_file: Optional[str]
    activity_status: Optional[ActivityStatus]
    is_active: bool = True
    status: bool = True

    class Config:
        orm_mode = True

# Modelo Pydantic para la creación de actividad
class ActivityCreate(ActivityBase):
    pass

# Modelo Pydantic para la actualización de actividad
class ActivityUpdate(ActivityBase):
    id: int

# Modelo Pydantic para la respuesta de actividad
class Activity(ActivityBase):
    id: int
    presenter: Optional[presenter]
    co_presenters: Optional[List[presenter]] = []
    type: Optional[typeActivities]

    class Config:
        orm_mode = True
