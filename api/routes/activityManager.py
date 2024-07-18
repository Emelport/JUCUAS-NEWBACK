from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.session import get_db
from schemas.activityManager import ActivityManagerCreate, ActivityManager, ActivityManagerUpdate
from models.activityManager import ActivityManager as DBActivityManager
from api.deps import get_current_user, group_required

router = APIRouter()

@router.get("/list/", response_model=List[ActivityManager])
def list_activity_managers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activity_managers = db.query(DBActivityManager).filter(DBActivityManager.status == True).offset(skip).limit(limit).all()
    return activity_managers

@router.post("/create/", response_model=ActivityManager)
def create_activity_manager(activity_manager: ActivityManagerCreate, db: Session = Depends(get_db)):
    db_activity_manager = DBActivityManager(**activity_manager.dict())
    db.add(db_activity_manager)
    db.commit()
    db.refresh(db_activity_manager)
    return db_activity_manager

@router.get("/{pk}/", response_model=ActivityManager)
def retrieve_activity_manager(pk: int, db: Session = Depends(get_db)):
    activity_manager = db.query(DBActivityManager).filter(DBActivityManager.id == pk, DBActivityManager.status == True).first()
    if activity_manager is None:
        raise HTTPException(status_code=404, detail="Activity Manager not found")
    return activity_manager

@router.put("/{pk}/", response_model=ActivityManager)
def update_activity_manager(pk: int, activity_manager: ActivityManagerUpdate, db: Session = Depends(get_db)):
    db_activity_manager = db.query(DBActivityManager).filter(DBActivityManager.id == pk, DBActivityManager.status == True).first()
    if db_activity_manager is None:
        raise HTTPException(status_code=404, detail="Activity Manager not found")
    for key, value in activity_manager.dict(exclude_unset=True).items():
        setattr(db_activity_manager, key, value)
    db.commit()
    db.refresh(db_activity_manager)
    return db_activity_manager

@router.delete("/{pk}/", response_model=ActivityManager)
def delete_activity_manager(pk: int, db: Session = Depends(get_db)):
    db_activity_manager = db.query(DBActivityManager).filter(DBActivityManager.id == pk, DBActivityManager.status == True).first()
    if db_activity_manager is None:
        raise HTTPException(status_code=404, detail="Activity Manager not found")
    db_activity_manager.is_active = False
    db_activity_manager.status = False
    db.commit()
    db.refresh(db_activity_manager)
    return db_activity_manager

@router.post("/current/", response_model=dict, dependencies=[Depends(get_current_user)])
def current_activity_manager(data: dict, db: Session = Depends(get_db)):
    # Implementación para verificar fechas límite si es necesario
    return {'status': 'Error', 'message': 'Endpoint not implemented'}

@router.post("/upload_file/", response_model=dict, dependencies=[Depends(get_current_user)])
def upload_file(file_data: dict, db: Session = Depends(get_db)):
    # Implementación para subir archivos si es necesario
    return {'status': 'Error', 'message': 'Endpoint not implemented'}

def current_date_to_upload_activities(db: Session):
    # Implementación para verificar fecha límite de subida de actividades
    return False

def current_date_to_upload_evidences(db: Session):
    # Implementación para verificar fecha límite de subida de evidencias
    return False

def current_date_to_validate_evidences(db: Session):
    # Implementación para verificar fecha límite de validación de evidencias
    return False
