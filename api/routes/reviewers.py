from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from schemas.reviewers import ReviewerCreate, Reviewer
from db.session import get_db
from models.reviewers import Reviewer as DBReviewer

router = APIRouter()

@router.get("/list/", response_model=List[Reviewer])
def list_reviewers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reviewers = db.query(DBReviewer).filter(DBReviewer.status == True).offset(skip).limit(limit).all()
    return reviewers

@router.post("/create/", response_model=Reviewer)
def create_reviewer(reviewer: ReviewerCreate, db: Session = Depends(get_db)):
    db_reviewer = DBReviewer(**reviewer.dict())
    db.add(db_reviewer)
    db.commit()
    db.refresh(db_reviewer)
    return db_reviewer

@router.get("/{pk}/", response_model=Reviewer)
def retrieve_reviewer(pk: int, db: Session = Depends(get_db)):
    reviewer = db.query(DBReviewer).filter(DBReviewer.id == pk, DBReviewer.status == True).first()
    if reviewer is None:
        raise HTTPException(status_code=404, detail="Reviewer not found")
    return reviewer

@router.put("/{pk}/", response_model=Reviewer)
def update_reviewer(pk: int, reviewer: ReviewerCreate, db: Session = Depends(get_db)):
    db_reviewer = db.query(DBReviewer).filter(DBReviewer.id == pk, DBReviewer.status == True).first()
    if db_reviewer is None:
        raise HTTPException(status_code=404, detail="Reviewer not found")
    for key, value in reviewer.dict().items():
        setattr(db_reviewer, key, value)
    db.commit()
    db.refresh(db_reviewer)
    return db_reviewer

@router.delete("/{pk}/", response_model=Reviewer)
def delete_reviewer(pk: int, db: Session = Depends(get_db)):
    db_reviewer = db.query(DBReviewer).filter(DBReviewer.id == pk, DBReviewer.status == True).first()
    if db_reviewer is None:
        raise HTTPException(status_code=404, detail="Reviewer not found")
    db_reviewer.is_active = False
    db_reviewer.status = False
    db.commit()
    db.refresh(db_reviewer)
    return db_reviewer
