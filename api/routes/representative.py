from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List


from schemas.representative import RepresentativeCreate, Representative
from db.session import get_db
from models.representative import Representative as DBRepresentative

router = APIRouter()

@router.get("/list/", response_model=List[Representative])
def list_representatives(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    representatives = db.query(DBRepresentative).filter(DBRepresentative.status == True).offset(skip).limit(limit).all()
    return representatives

@router.post("/create/", response_model=Representative)
def create_representative(representative: RepresentativeCreate, db: Session = Depends(get_db)):
    db_representative = DBRepresentative(**representative.dict())
    db.add(db_representative)
    db.commit()
    db.refresh(db_representative)
    return db_representative

@router.get("/{pk}/", response_model=Representative)
def retrieve_representative(pk: int, db: Session = Depends(get_db)):
    representative = db.query(DBRepresentative).filter(DBRepresentative.id == pk, DBRepresentative.status == True).first()
    if representative is None:
        raise HTTPException(status_code=404, detail="Representative not found")
    return representative

@router.put("/{pk}/", response_model=Representative)
def update_representative(pk: int, representative: RepresentativeCreate, db: Session = Depends(get_db)):
    db_representative = db.query(DBRepresentative).filter(DBRepresentative.id == pk, DBRepresentative.status == True).first()
    if db_representative is None:
        raise HTTPException(status_code=404, detail="Representative not found")
    for key, value in representative.dict().items():
        setattr(db_representative, key, value)
    db.commit()
    db.refresh(db_representative)
    return db_representative

@router.delete("/{pk}/", response_model=Representative)
def delete_representative(pk: int, db: Session = Depends(get_db)):
    db_representative = db.query(DBRepresentative).filter(DBRepresentative.id == pk, DBRepresentative.status == True).first()
    if db_representative is None:
        raise HTTPException(status_code=404, detail="Representative not found")
    db_representative.is_active = False
    db_representative.status = False
    db.commit()
    db.refresh(db_representative)
    return db_representative