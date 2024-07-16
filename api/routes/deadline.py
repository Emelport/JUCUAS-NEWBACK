# api/routes/deadline.py

from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models.deadline import Deadline as DBDeadline  # Ajusta la importación según tus necesidades
from schemas.deadline import DeadlineCreate, Deadline, DeadlineUpdate, DeadlineUploadFile  # Ajusta la importación según tus necesidades
from db.session  import get_db  # Ajusta la importación según tus necesidades
from api.deps import get_current_user, group_required  # Ajusta la importación según tus necesidades

router = APIRouter()

@router.get("/list/", response_model=List[Deadline])
def list_deadlines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    deadlines = db.query(DBDeadline).filter(DBDeadline.status == True).offset(skip).limit(limit).all()
    return deadlines

@router.post("/create/", response_model=Deadline, dependencies=[Depends(group_required(['admin', 'representative', 'reviewer']))])
def create_deadline(deadline: DeadlineCreate, db: Session = Depends(get_db)):
    db_deadline = DBDeadline(**deadline.dict())
    db.add(db_deadline)
    db.commit()
    db.refresh(db_deadline)
    return db_deadline

@router.get("/{pk}/", response_model=Deadline)
def retrieve_deadline(pk: int, db: Session = Depends(get_db)):
    deadline = db.query(DBDeadline).filter(DBDeadline.id == pk, DBDeadline.status == True).first()
    if deadline is None:
        raise HTTPException(status_code=404, detail="Deadline not found")
    return deadline

@router.put("/{pk}/", response_model=Deadline, dependencies=[Depends(group_required(['admin', 'representative', 'reviewer']))])
def update_deadline(pk: int, deadline: DeadlineUpdate, db: Session = Depends(get_db)):
    db_deadline = db.query(DBDeadline).filter(DBDeadline.id == pk, DBDeadline.status == True).first()
    if db_deadline is None:
        raise HTTPException(status_code=404, detail="Deadline not found")
    for key, value in deadline.dict().items():
        setattr(db_deadline, key, value)
    db.commit()
    db.refresh(db_deadline)
    return db_deadline

@router.delete("/{pk}/", response_model=Deadline, dependencies=[Depends(group_required(['admin', 'representative', 'reviewer']))])
def delete_deadline(pk: int, db: Session = Depends(get_db)):
    db_deadline = db.query(DBDeadline).filter(DBDeadline.id == pk, DBDeadline.status == True).first()
    if db_deadline is None:
        raise HTTPException(status_code=404, detail="Deadline not found")
    db_deadline.is_active = False
    db_deadline.status = False
    db.commit()
    db.refresh(db_deadline)
    return db_deadline

@router.post("/current/", response_model=dict, dependencies=[Depends(get_current_user)])
def current_deadline(data: dict, db: Session = Depends(get_db)):
    if data['deadline'] == 'upload_activities':
        if current_date_to_upload_activities(db):
            return {'status': 'OK'}
        return {'status': 'Error', 'message': 'La fecha limite para subir actividades ya paso'}

    elif data['deadline'] == 'upload_evidences':
        if current_date_to_upload_evidences(db):
            return {'status': 'OK'}
        return {'status': 'Error', 'message': 'La fecha limite para subir evidencias ya paso'}

    elif data['deadline'] == 'validate_evidences':
        if current_date_to_validate_evidences(db):
            return {'status': 'OK'}
        return {'status': 'Error', 'message': 'La fecha limite para validar evidencias ya paso'}

    return {'status': 'Error', 'message': 'Hubo un error con las fechas limite'}

@router.post("/upload_file/", response_model=dict, dependencies=[Depends(get_current_user)])
def upload_file(file_data: DeadlineUploadFile, db: Session = Depends(get_db)):
    id = file_data.id
    file_name = file_data.file_name
    file = file_data.file
    evidence_obj = db.query(DBDeadline).get(id)
    evidence_obj.file = file
    evidence_obj.file_name = file_name
    db.commit()
    return {'status': 'OK', 'message': 'Archivo subido'}

def current_date_to_upload_activities(db: Session):
    date = datetime.now().date()
    current = db.query(DBDeadline).filter(DBDeadline.date_edition == date.year, DBDeadline.status == 1).first()
    return date < current.date_to_upload_activities

def current_date_to_upload_evidences(db: Session):
    date = datetime.now().date()
    current = db.query(DBDeadline).filter(DBDeadline.date_edition == date.year, DBDeadline.status == 1).first()
    return date < current.date_to_upload_evidence

def current_date_to_validate_evidences(db: Session):
    date = datetime.now().date()
    current = db.query(DBDeadline).order_by(DBDeadline.id.desc()).first()
    return date < current.date_to_validate_evidence
