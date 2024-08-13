from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from models.choices import Modality, EducationalLevel, TypeOfPublic, AreaKnowledge, ActivityStatus
from schemas.presenter import Presenter  # Asegúrate de que este modelo Pydantic esté definido correctamente
from schemas.typeActivities import TypeActivity  # Asegúrate de que este modelo Pydantic esté definido correctamente

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
        from_attributes = True

# Modelo Pydantic para la creación de actividad
class ActivityCreate(ActivityBase):
    pass

# Modelo Pydantic para la actualización de actividad
class ActivityUpdate(ActivityBase):
    id: int

# Modelo Pydantic para la respuesta de actividad
class Activity(ActivityBase):
    id: int
    presenter: Optional[Presenter]
    co_presenters: Optional[List[Presenter]] = []
    type: Optional[TypeActivity]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
