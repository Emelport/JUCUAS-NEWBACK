from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from schemas.universities import UniversityCreate, University
from db.session import get_db
from models.universities import University as DBUniversity

router = APIRouter()

@router.get("/list/", response_model=List[University])
def list_universities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    universities = db.query(DBUniversity).filter(DBUniversity.status == True).offset(skip).limit(limit).all()
    return universities

@router.post("/create/", response_model=University)
def create_university(university: UniversityCreate, db: Session = Depends(get_db)):
    db_university = DBUniversity(**university.dict())
    db.add(db_university)
    db.commit()
    db.refresh(db_university)
    return db_university

@router.get("/{pk}/", response_model=University)
def retrieve_university(pk: int, db: Session = Depends(get_db)):
    university = db.query(DBUniversity).filter(DBUniversity.id == pk, DBUniversity.status == True).first()
    if university is None:
        raise HTTPException(status_code=404, detail="University not found")
    return university

@router.put("/{pk}/", response_model=University)
def update_university(pk: int, university: UniversityCreate, db: Session = Depends(get_db)):
    db_university = db.query(DBUniversity).filter(DBUniversity.id == pk, DBUniversity.status == True).first()
    if db_university is None:
        raise HTTPException(status_code=404, detail="University not found")
    for key, value in university.dict().items():
        setattr(db_university, key, value)
    db.commit()
    db.refresh(db_university)
    return db_university

@router.delete("/{pk}/", response_model=University)
def delete_university(pk: int, db: Session = Depends(get_db)):
    db_university = db.query(DBUniversity).filter(DBUniversity.id == pk, DBUniversity.status == True).first()
    if db_university is None:
        raise HTTPException(status_code=404, detail="University not found")
    db_university.is_active = False
    db_university.status = False
    db.commit()
    db.refresh(db_university)
    return db_university

@router.get("/table/", response_model=List[University])
def table_universities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    universities = db.query(DBUniversity).filter(DBUniversity.status == True).offset(skip).limit(limit).all()
    return universities