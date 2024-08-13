# api/routes/auth.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import timedelta, datetime

from core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from schemas.tokens import Token, TokenCreate
from core.security import verify_password, create_access_token
from db.session import get_db
from models.users import User as DBUser

router = APIRouter()

@router.post("/token/", response_model=Token)
def login(token_request: TokenCreate, db: Session = Depends(get_db)):
    user = db.query(DBUser).filter(DBUser.username == token_request.username).first()
    if not user or not verify_password(token_request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Crear un token de acceso
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + access_token_expires
    }
