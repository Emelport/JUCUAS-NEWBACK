from fastapi import APIRouter, HTTPException, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta, datetime
from typing import Optional

from core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from schemas.tokens import Token
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
