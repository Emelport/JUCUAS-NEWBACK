from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.session import get_db
from schemas.typeEvidence import TypeEvidenceCreate, TypeEvidence, TypeEvidenceUpdate
from models.typeEvidence import TypeEvidence as DBTypeEvidence
from api.deps import get_current_user

router = APIRouter()

@router.get("/type/evidence/list/", response_model=List[TypeEvidence])
def list_type_evidences(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    type_evidences = db.query(DBTypeEvidence).offset(skip).limit(limit).all()
    return type_evidences

@router.post("/type/evidence/create/", response_model=TypeEvidence)
def create_type_evidence(type_evidence: TypeEvidenceCreate, db: Session = Depends(get_db)):
    db_type_evidence = DBTypeEvidence(**type_evidence.dict())
    db.add(db_type_evidence)
    db.commit()
    db.refresh(db_type_evidence)
    return db_type_evidence

@router.get("/type/evidence/{pk}/", response_model=TypeEvidence)
def retrieve_type_evidence(pk: int, db: Session = Depends(get_db)):
    type_evidence = db.query(DBTypeEvidence).filter(DBTypeEvidence.id == pk).first()
    if type_evidence is None:
        raise HTTPException(status_code=404, detail="Type evidence not found")
    return type_evidence

@router.put("/type/evidence/{pk}/", response_model=TypeEvidence)
def update_type_evidence(pk: int, type_evidence: TypeEvidenceUpdate, db: Session = Depends(get_db)):
    db_type_evidence = db.query(DBTypeEvidence).filter(DBTypeEvidence.id == pk).first()
    if db_type_evidence is None:
        raise HTTPException(status_code=404, detail="Type evidence not found")
    for key, value in type_evidence.dict(exclude_unset=True).items():
        setattr(db_type_evidence, key, value)
    db.commit()
    db.refresh(db_type_evidence)
    return db_type_evidence

@router.delete("/type/evidence/{pk}/", response_model=TypeEvidence)
def delete_type_evidence(pk: int, db: Session = Depends(get_db)):
    db_type_evidence = db.query(DBTypeEvidence).filter(DBTypeEvidence.id == pk).first()
    if db_type_evidence is None:
        raise HTTPException(status_code=404, detail="Type evidence not found")
    db.delete(db_type_evidence)
    db.commit()
    return {"detail": "Type evidence deleted"}
