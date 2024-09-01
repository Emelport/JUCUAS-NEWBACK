from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List

from schemas.groups import GroupCreate
from schemas.users import User, UserCreate, Token, UserUpdate, UserResponse
from models.users import User as SQLUser, Group
from core.security import verify_password, get_password_hash, create_access_token
from api.deps import get_db, get_current_user
from core.config import *

router = APIRouter()

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(SQLUser).filter(SQLUser.email == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


@router.post("/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica si el email ya está registrado
    db_user = db.query(SQLUser).filter(SQLUser.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Crea el nuevo usuario
    hashed_password = get_password_hash(user.password)
    db_user = SQLUser(
        username=user.username,
        email=user.email,
        password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        gender=user.gender,
        phone=user.phone
    )

    # Asigna los grupos si se proporcionan
    if user.groups:
        groups = db.query(Group).filter(Group.id.in_(user.groups)).all()
        if len(groups) != len(user.groups):
            raise HTTPException(status_code=400, detail="One or more groups do not exist")
        db_user.groups.extend(groups)

    # Guarda el usuario en la base de datos
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    # Busca el usuario
    db_user = db.query(SQLUser).filter(SQLUser.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Actualiza los campos del usuario
    if user_update.username:
        db_user.username = user_update.username
    if user_update.email:
        db_user.email = user_update.email
    if user_update.first_name:
        db_user.first_name = user_update.first_name
    if user_update.last_name:
        db_user.last_name = user_update.last_name
    if user_update.gender:
        db_user.gender = user_update.gender
    if user_update.phone:
        db_user.phone = user_update.phone

    # Actualiza los grupos
    if user_update.groups is not None:
        # Borra las asociaciones existentes
        db_user.groups = []
        # Añade las nuevas asociaciones
        groups = db.query(Group).filter(Group.id.in_(user_update.groups)).all()
        if len(groups) != len(user_update.groups):
            raise HTTPException(status_code=400, detail="One or more groups do not exist")
        db_user.groups.extend(groups)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Convertir a UserResponse con nombres de grupos
    user_response = UserResponse(
        username=db_user.username,
        email=db_user.email,
        first_name=db_user.first_name,
        last_name=db_user.last_name,
        gender=db_user.gender,
        phone=db_user.phone,
        groups=[group.name for group in db_user.groups]
    )

    return user_response


@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(SQLUser).offset(skip).limit(limit).all()
    return users

@router.post("/groups", response_model=GroupCreate)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    # Verifica si el grupo ya existe
    existing_group = db.query(Group).filter(Group.name == group.name).first()
    if existing_group:
        raise HTTPException(status_code=400, detail="Group already exists")

    # Crea el nuevo grupo
    db_group = Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)

    return db_group