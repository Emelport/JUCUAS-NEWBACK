from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.session import get_db
from models.presenter import Presenter as DBPresenter
from schemas.presenter import (
    PresenterCreate, Presenter, PresenterUpdateGender,
    PresenterUpdateName, PresenterUpdatePhone, PresenterUpdateEmail
)

router = APIRouter()

@router.get("/list/", response_model=List[Presenter])
def list_presenters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    presenters = db.query(DBPresenter).filter(DBPresenter.status == True).offset(skip).limit(limit).all()
    return presenters

@router.post("/create/", response_model=Presenter)
def create_presenter(presenter: PresenterCreate, db: Session = Depends(get_db)):
    db_presenter = DBPresenter(**presenter.dict())
    db.add(db_presenter)
    db.commit()
    db.refresh(db_presenter)
    return db_presenter

@router.get("/{pk}/", response_model=Presenter)
def retrieve_presenter(pk: int, db: Session = Depends(get_db)):
    presenter = db.query(DBPresenter).filter(DBPresenter.id == pk, DBPresenter.status == True).first()
    if presenter is None:
        raise HTTPException(status_code=404, detail="Presenter not found")
    return presenter

@router.put("/{pk}/", response_model=Presenter)
def update_presenter(pk: int, presenter: PresenterCreate, db: Session = Depends(get_db)):
    db_presenter = db.query(DBPresenter).filter(DBPresenter.id == pk, DBPresenter.status == True).first()
    if db_presenter is None:
        raise HTTPException(status_code=404, detail="Presenter not found")
    for key, value in presenter.dict().items():
        setattr(db_presenter, key, value)
    db.commit()
    db.refresh(db_presenter)
    return db_presenter

@router.delete("/{pk}/", response_model=Presenter)
def delete_presenter(pk: int, db: Session = Depends(get_db)):
    db_presenter = db.query(DBPresenter).filter(DBPresenter.id == pk, DBPresenter.status == True).first()
    if db_presenter is None:
        raise HTTPException(status_code=404, detail="Presenter not found")
    db_presenter.is_active = False
    db_presenter.status = False
    db.commit()
    db.refresh(db_presenter)
    return db_presenter

@router.get("/verify/")
def verify_exist(email: str, db: Session = Depends(get_db)):
    presenter = db.query(DBPresenter).filter(DBPresenter.email == email).first()
    if presenter:
        return {"exists": True}
    return {"exists": False}

@router.get("/current/", response_model=Presenter)
def current_presenter(db: Session = Depends(get_db)):
    # Aquí puedes obtener el presentador actual de la sesión o el token
    presenter_id = 1  # Esto es solo un ejemplo, debes obtener el ID real del presentador actual
    presenter = db.query(DBPresenter).filter(DBPresenter.id == presenter_id).first()
    if presenter is None:
        raise HTTPException(status_code=404, detail="Presenter not found")
    return presenter

@router.patch("/update_gender/", response_model=Presenter)
def update_gender(presenter_id: int, gender: PresenterUpdateGender, db: Session = Depends(get_db)):
    db_presenter = db.query(DBPresenter).filter(DBPresenter.id == presenter_id).first()
    if db_presenter is None:
        raise HTTPException(status_code=404, detail="Presenter not found")
    db_presenter.gender = gender.gender
    db.commit()
    db.refresh(db_presenter)
    return db_presenter

@router.patch("/update_name/", response_model=Presenter)
def update_name(presenter_id: int, name: PresenterUpdateName, db: Session = Depends(get_db)):
    db_presenter = db.query(DBPresenter).filter(DBPresenter.id == presenter_id).first()
    if db_presenter is None:
        raise HTTPException(status_code=404, detail="Presenter not found")
    db_presenter.first_name = name.first_name
    db_presenter.last_name = name.last_name
    db.commit()
    db.refresh(db_presenter)
    return db_presenter

@router.patch("/update_phone/", response_model=Presenter)
def update_phone(presenter_id: int, phone: PresenterUpdatePhone, db: Session = Depends(get_db)):
    db_presenter = db.query(DBPresenter).filter(DBPresenter.id == presenter_id).first()
    if db_presenter is None:
        raise HTTPException(status_code=404, detail="Presenter not found")
    db_presenter.phone = phone.phone
    db.commit()
    db.refresh(db_presenter)
    return db_presenter

@router.patch("/update_email/", response_model=Presenter)
def update_email(presenter_id: int, email: PresenterUpdateEmail, db: Session = Depends(get_db)):
    db_presenter = db.query(DBPresenter).filter(DBPresenter.id == presenter_id).first()
    if db_presenter is None:
        raise HTTPException(status_code=404, detail="Presenter not found")
    db_presenter.email = email.email
    db.commit()
    db.refresh(db_presenter)
    return db_presenter

@router.get("/filteredlist/", response_model=List[Presenter])
def get_filteredlist(filter: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    presenters = db.query(DBPresenter).filter(DBPresenter.first_name.contains(filter) | DBPresenter.last_name.contains(filter), DBPresenter.status == True).offset(skip).limit(limit).all()
    return presenters

@router.get("/filteredlisttable/", response_model=List[Presenter])
def get_filteredlisttable(filter: str, page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    offset = (page - 1) * page_size
    limit = page_size
    presenters = db.query(DBPresenter).filter(DBPresenter.first_name.contains(filter) | DBPresenter.last_name.contains(filter), DBPresenter.status == True).offset(offset).limit(limit).all()
    count = db.query(DBPresenter).filter(DBPresenter.first_name.contains(filter) | DBPresenter.last_name.contains(filter), DBPresenter.status == True).count()
    return {"count": count, "results": presenters, "next": f"presenters/filteredlisttable/?page={page + 1}&page_size={page_size}" if count > offset + limit else None, "previous": f"presenters/filteredlisttable/?page={page - 1}&page_size={page_size}" if page > 1 else None}

@router.get("/get_copresenter/", response_model=List[Presenter])
def get_copresenter(id: int, db: Session = Depends(get_db)):
    copresenters = db.query(DBPresenter).filter(DBPresenter.id == id, DBPresenter.status == True).all()
    return copresenters
