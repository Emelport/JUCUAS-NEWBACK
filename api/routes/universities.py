from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from schemas.universities import UniversityCreate, University  # Asegúrate de importar el esquema University desde schemas.universities
from db.session import get_db
from models.universities import University as DBUniversity

router = APIRouter()

# Traer todas las universidades
@router.get("/universities", response_model=List[University])
def read_universities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    universities = db.query(DBUniversity).offset(skip).limit(limit).all()
    return universities

# Crear una universidad
@router.post("/universities", response_model=University)
def create_university(university: UniversityCreate, db: Session = Depends(get_db)):
    db_university = DBUniversity(
        name=university.name, acronym=university.acronym, key_code=university.key_code,
        type=university.type, region=university.region, municipality=university.municipality,
        locality=university.locality, email=university.email, phone=university.phone
    )
    db.add(db_university)
    db.commit()
    db.refresh(db_university)
    return db_university
