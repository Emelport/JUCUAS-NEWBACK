from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List

from schemas.users import User, UserCreate, Token
from models.users import User as SQLUser
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

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(SQLUser).filter(SQLUser.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    db_user = SQLUser(
        username=user.username, email=user.email, password=hashed_password,
        first_name=user.first_name, last_name=user.last_name,
        gender=user.gender, phone=user.phone
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(SQLUser).offset(skip).limit(limit).all()
    return users

@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
