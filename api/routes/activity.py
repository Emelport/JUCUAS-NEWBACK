from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.session import get_db
from schemas.activity import ActivityCreate, Activity, ActivityUpdate
from models.activities import Activity as DBActivity

router = APIRouter()

@router.get("/list/", response_model=List[Activity])
def list_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = db.query(DBActivity).offset(skip).limit(limit).all()
    return activities

@router.post("/create/", response_model=Activity)
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    db_activity = DBActivity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

@router.get("/{pk}/", response_model=Activity)
def retrieve_activity(pk: int, db: Session = Depends(get_db)):
    activity = db.query(DBActivity).filter(DBActivity.id == pk).first()
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity

@router.put("/{pk}/", response_model=Activity)
def update_activity(pk: int, activity: ActivityUpdate, db: Session = Depends(get_db)):
    db_activity = db.query(DBActivity).filter(DBActivity.id == pk).first()
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    for key, value in activity.dict(exclude_unset=True).items():
        setattr(db_activity, key, value)
    db.commit()
    db.refresh(db_activity)
    return db_activity

@router.delete("/{pk}/")
def delete_activity(pk: int, db: Session = Depends(get_db)):
    db_activity = db.query(DBActivity).filter(DBActivity.id == pk).first()
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    db.delete(db_activity)
    db.commit()
    return {"detail": "Activity deleted"}

@router.patch("/partial/activity/{pk}/", response_model=Activity)
def partial_update_activity(pk: int, activity: ActivityUpdate, db: Session = Depends(get_db)):
    db_activity = db.query(DBActivity).filter(DBActivity.id == pk).first()
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    for key, value in activity.dict(exclude_unset=True).items():
        setattr(db_activity, key, value)
    db.commit()
    db.refresh(db_activity)
    return db_activity

@router.patch("/partial/pdf/{pk}/", response_model=Activity)
def partial_update_save_pdf(pk: int, activity: ActivityUpdate, db: Session = Depends(get_db)):
    db_activity = db.query(DBActivity).filter(DBActivity.id == pk).first()
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    for key, value in activity.dict(exclude_unset=True).items():
        setattr(db_activity, key, value)
    db.commit()
    db.refresh(db_activity)
    return db_activity

@router.get("/list/presenter/", response_model=List[Activity])
def list_activities_by_presenter(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = db.query(DBActivity).filter(DBActivity.presenter_id != None).offset(skip).limit(limit).all()
    return activities

@router.get("/list/representer/", response_model=List[Activity])
def list_activities_by_representer(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = db.query(DBActivity).filter(DBActivity.representer_id != None).offset(skip).limit(limit).all()
    return activities

@router.get("/list/region/", response_model=List[Activity])
def list_activities_by_region(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = db.query(DBActivity).filter(DBActivity.region_id != None).offset(skip).limit(limit).all()
    return activities

@router.get("/list/activity_constansy/", response_model=List[Activity])
def list_activity_constansy(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = db.query(DBActivity).filter(DBActivity.constansy == True).offset(skip).limit(limit).all()
    return activities

@router.get("/filteredlisttable/", response_model=List[Activity])
def get_filtered_list_table(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = db.query(DBActivity).offset(skip).limit(limit).all()
    return activities

@router.get("/statistics/", response_model=dict)
def get_statistics(db: Session = Depends(get_db)):
    total_activities = db.query(DBActivity).count()
    active_activities = db.query(DBActivity).filter(DBActivity.status == True).count()
    return {"total_activities": total_activities, "active_activities": active_activities}
