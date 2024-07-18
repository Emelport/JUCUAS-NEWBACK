from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.session import get_db
from schemas.typeActivities import TypeActivityCreate, TypeActivity, TypeActivityUpdate
from models.typeActivities import TypeActivity as DBTypeActivity
from api.deps import get_current_user

router = APIRouter()

@router.get("/type/activity/list/", response_model=List[TypeActivity])
def list_type_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    type_activities = db.query(DBTypeActivity).offset(skip).limit(limit).all()
    return type_activities

@router.post("/type/activity/create/", response_model=TypeActivity)
def create_type_activity(type_activity: TypeActivityCreate, db: Session = Depends(get_db)):
    db_type_activity = DBTypeActivity(**type_activity.dict())
    db.add(db_type_activity)
    db.commit()
    db.refresh(db_type_activity)
    return db_type_activity

@router.get("/type/activity/{pk}/", response_model=TypeActivity)
def retrieve_type_activity(pk: int, db: Session = Depends(get_db)):
    type_activity = db.query(DBTypeActivity).filter(DBTypeActivity.id == pk).first()
    if type_activity is None:
        raise HTTPException(status_code=404, detail="Type activity not found")
    return type_activity

@router.put("/type/activity/{pk}/", response_model=TypeActivity)
def update_type_activity(pk: int, type_activity: TypeActivityUpdate, db: Session = Depends(get_db)):
    db_type_activity = db.query(DBTypeActivity).filter(DBTypeActivity.id == pk).first()
    if db_type_activity is None:
        raise HTTPException(status_code=404, detail="Type activity not found")
    for key, value in type_activity.dict(exclude_unset=True).items():
        setattr(db_type_activity, key, value)
    db.commit()
    db.refresh(db_type_activity)
    return db_type_activity

@router.delete("/type/activity/{pk}/", response_model=TypeActivity)
def delete_type_activity(pk: int, db: Session = Depends(get_db)):
    db_type_activity = db.query(DBTypeActivity).filter(DBTypeActivity.id == pk).first()
    if db_type_activity is None:
        raise HTTPException(status_code=404, detail="Type activity not found")
    db.delete(db_type_activity)
    db.commit()
    return {"detail": "Type activity deleted"}
