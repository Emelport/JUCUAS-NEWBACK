from pydantic import BaseModel

# Modelo Pydantic para la relación entre Activity y Presenter (ActivityCoPresenter)
class ActivityCoPresenter(BaseModel):
    activity_id: int
    co_presenter_id: int

    class Config:
        orm_mode = True
