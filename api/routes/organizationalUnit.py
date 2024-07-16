from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List

from schemas.organizationalUnit import OrganizationalUnitCreate, OrganizationalUnit
from db.session import get_db
from models.organizationalUnit import OrganizationalUnit as DBOrganizationalUnit

router = APIRouter()


@router.get("/list/", response_model=List[OrganizationalUnit])
def list_organizational_units(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    units = db.query(DBOrganizationalUnit).filter(DBOrganizationalUnit.status == True).offset(skip).limit(limit).all()
    return units

@router.post("/create/", response_model=OrganizationalUnit)
def create_organizational_unit(unit: OrganizationalUnitCreate, db: Session = Depends(get_db)):
    db_unit = DBOrganizationalUnit(**unit.dict())
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit

@router.get("/{pk}/", response_model=OrganizationalUnit)
def retrieve_organizational_unit(pk: int, db: Session = Depends(get_db)):
    unit = db.query(DBOrganizationalUnit).filter(DBOrganizationalUnit.id == pk, DBOrganizationalUnit.status == True).first()
    if unit is None:
        raise HTTPException(status_code=404, detail="Organizational Unit not found")
    return unit

@router.put("/{pk}/", response_model=OrganizationalUnit)
def update_organizational_unit(pk: int, unit: OrganizationalUnitCreate, db: Session = Depends(get_db)):
    db_unit = db.query(DBOrganizationalUnit).filter(DBOrganizationalUnit.id == pk, DBOrganizationalUnit.status == True).first()
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Organizational Unit not found")
    for key, value in unit.dict().items():
        setattr(db_unit, key, value)
    db.commit()
    db.refresh(db_unit)
    return db_unit

@router.delete("/{pk}/", response_model=OrganizationalUnit)
def delete_organizational_unit(pk: int, db: Session = Depends(get_db)):
    db_unit = db.query(DBOrganizationalUnit).filter(DBOrganizationalUnit.id == pk, DBOrganizationalUnit.status == True).first()
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Organizational Unit not found")
    db_unit.is_active = False
    db_unit.status = False
    db.commit()
    db.refresh(db_unit)
    return db_unit