from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.session import get_db
from schemas.evidence import EvidenceCreate, Evidence, EvidenceUpdate
from models.evidence import Evidence as DBEvidence
from api.deps import get_current_user

router = APIRouter()

@router.get("/evidence/list/", response_model=List[Evidence])
def list_evidences(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    evidences = db.query(DBEvidence).offset(skip).limit(limit).all()
    return evidences

@router.post("/evidence/create/", response_model=Evidence)
def create_evidence(evidence: EvidenceCreate, db: Session = Depends(get_db)):
    db_evidence = DBEvidence(**evidence.dict())
    db.add(db_evidence)
    db.commit()
    db.refresh(db_evidence)
    return db_evidence

@router.get("/evidence/{pk}/", response_model=Evidence)
def retrieve_evidence(pk: int, db: Session = Depends(get_db)):
    evidence = db.query(DBEvidence).filter(DBEvidence.id == pk).first()
    if evidence is None:
        raise HTTPException(status_code=404, detail="Evidence not found")
    return evidence

@router.put("/evidence/{pk}/", response_model=Evidence)
def update_evidence(pk: int, evidence: EvidenceUpdate, db: Session = Depends(get_db)):
    db_evidence = db.query(DBEvidence).filter(DBEvidence.id == pk).first()
    if db_evidence is None:
        raise HTTPException(status_code=404, detail="Evidence not found")
    for key, value in evidence.dict(exclude_unset=True).items():
        setattr(db_evidence, key, value)
    db.commit()
    db.refresh(db_evidence)
    return db_evidence

@router.patch("/evidence/validate/{pk}/", response_model=Evidence)
def validate_evidence(pk: int, evidence: EvidenceUpdate, db: Session = Depends(get_db)):
    db_evidence = db.query(DBEvidence).filter(DBEvidence.id == pk).first()
    if db_evidence is None:
        raise HTTPException(status_code=404, detail="Evidence not found")
    db_evidence.validated = True
    db.commit()
    db.refresh(db_evidence)
    return db_evidence

@router.post("/evidence/updateTables", response_model=dict)
def update_activity_evidence(db: Session = Depends(get_db)):
    # Implementación para actualizar tablas de evidencia
    return {'status': 'Error', 'message': 'Endpoint not implemented'}

@router.get("/evidencesforactivity/{activity_id}/", response_model=List[Evidence])
def get_evidences_for_activity(activity_id: int, db: Session = Depends(get_db)):
    evidences = db.query(DBEvidence).filter(DBEvidence.activity_id == activity_id).all()
    return evidences

@router.post("/qr_generator/", response_model=dict)
def qr_generator(data: dict, db: Session = Depends(get_db)):
    # Implementación para generar códigos QR
    return {'status': 'Error', 'message': 'Endpoint not implemented'}

@router.post("/pyjwt_generator/", response_model=dict)
def pyjwt_generator(data: dict, db: Session = Depends(get_db)):
    # Implementación para generar tokens JWT
    return {'status': 'Error', 'message': 'Endpoint not implemented'}

@router.post("/pyjwt_verify_qr/", response_model=dict)
def pyjwt_verify_qr(data: dict, db: Session = Depends(get_db)):
    # Implementación para verificar códigos QR con JWT
    return {'status': 'Error', 'message': 'Endpoint not implemented'}

@router.post("/send_certificate/", response_model=dict)
def send_certificate(data: dict, db: Session = Depends(get_db)):
    # Implementación para enviar certificados
    return {'status': 'Error', 'message': 'Endpoint not implemented'}
