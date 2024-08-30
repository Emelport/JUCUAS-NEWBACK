from fastapi import APIRouter, HTTPException, Depends, Form, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta, datetime
from typing import Optional, Union

from core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from schemas.tokens import Token
from schemas.users import LoginData
from core.security import verify_password, create_access_token
from db.session import get_db
from models.users import User as DBUser
from models.oauth_client import OAuthClient as DBClient

router = APIRouter()

@router.post("/token", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    client_id: Optional[str] = Form(None),
    client_secret: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    # Imprimir parámetros recibidos
    print("form_data:", form_data)
    print("client_id:", client_id)
    print("client_secret:", client_secret)

    if form_data.username and form_data.password:
        # Autenticación de usuario
        user = db.query(DBUser).filter(DBUser.username == form_data.username).first()
        if not user or not verify_password(form_data.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid user credentials")
        subject = user.username
    elif client_id and client_secret:
        # Autenticación de cliente
        client = db.query(DBClient).filter(DBClient.client_id == client_id).first()
        if not client or client.client_secret != client_secret:
            raise HTTPException(status_code=401, detail="Invalid client credentials")
        subject = client.client_id
    else:
        raise HTTPException(status_code=400, detail="Must provide either user credentials or client credentials")

    # Crear un token de acceso
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": subject},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + access_token_expires
    }


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user or not verify_password(password, user.password):
        return False
    return user

@router.post("/login", response_model=Token)
def login_for_access_token(
    login_data: LoginData,  # Acepta JSON como un objeto LoginData
    db: Session = Depends(get_db)
):
    username = login_data.username
    password = login_data.password

    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = create_refresh_token(
        data={"sub": user.username},
        expires_delta=refresh_token_expires
    )

    expires_at = datetime.utcnow() + access_token_expires

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "created_at": datetime.utcnow(),
        "expires_at": expires_at.isoformat(),  # Asegúrate de que esto sea un string en formato ISO
        "expires_in": int(access_token_expires.total_seconds())  # Tiempo en segundos hasta que expire el token
    }

def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=30)  # Expira en 30 días por defecto

    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt