
from fastapi import APIRouter, HTTPException, Depends, Form, status, Header
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import timedelta, datetime
from typing import Optional, Dict
from api.deps import get_current_user
from core.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from models.revokedTokens import RevokedToken
from schemas.tokens import Token
from schemas.users import LoginData, User, ChangePassword, UserOut
from models.users import User as DBUser
from core.security import verify_password, create_access_token, get_password_hash
from db.session import get_db
from models.oauth_client import OAuthClient as DBClient

router = APIRouter()


class UpdateGender(BaseModel):
    gender: str



def authenticate_user(db: Session, username: str, password: str):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user or not verify_password(password, user.password):
        return False
    return user


def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=30)  # Expira en 30 días por defecto

    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/login", response_model=Token)
def login_for_access_token(
    login_data: LoginData,
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

    # Crear access_token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    # Crear refresh_token
    refresh_token_expires = timedelta(days=30)
    refresh_token = create_refresh_token(
        data={"sub": user.username},
        expires_delta=refresh_token_expires
    )

    # Fecha de expiración del access_token
    expires_at = datetime.utcnow() + access_token_expires

    # Respuesta que incluye access_token y refresh_token
    response = {
        "access_token": access_token,
        "refresh_token": refresh_token,  # Asegúrate de que este valor esté presente
        "token_type": "bearer",
        "created_at": datetime.utcnow(),
        "expires_at": expires_at.isoformat(),
        "expires_in": int(access_token_expires.total_seconds())
    }

    # print("Response:", response)  # Para depuración, verifica lo que se está incluyendo en la respuesta

    return response


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(
        authorization: str = Header(None),
        db: Session = Depends(get_db)
):
    if authorization is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing")

    # Extraer el token del encabezado Authorization
    token = authorization.split(" ")[1]

    # Guardar el token en la tabla de tokens revocados
    revoked_token = RevokedToken(token=token)
    db.add(revoked_token)
    db.commit()

    return {"detail": "Successfully logged out"}



@router.get("/users/current", response_model=UserOut)
async def get_current_user(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    user_data = {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "gender": user.gender.name,  # Convierte el enum a string
        "phone": user.phone,
        "is_active": user.is_active,
        "is_superuser": user.is_superuser,
        "groups": [{"id": group.id, "name": group.name} for group in user.groups]  # Detalles del grupo
    }
    return user_data

# /my_gender saca el género del usuario actual
@router.post("/my_gender", response_model=Dict[str, str])
async def read_my_gender(current_user: User = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=401, detail="User not authenticated")

    return {"gender": current_user.get("gender")}


@router.post("/update_gender", response_model=User)
async def update_gender(
    update_data: UpdateGender,
    current_user: DBUser = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verifica si el género proporcionado es válido
    if update_data.gender not in ['H', 'M', 'O']:  # 'H' es hombre, 'M' es mujer, 'O' es otro
        raise HTTPException(status_code=400, detail="Invalid gender")

    # Actualiza el género del usuario actual
    current_user.gender = update_data.gender
    db.add(current_user)
    db.commit()
    db.refresh(current_user)

    # Devuelve el usuario actualizado como respuesta
    return current_user

@router.post("/password/change")
async def change_password(
        change_data: ChangePassword,
        current_user: DBUser = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    if not verify_password(change_data.actual_password, current_user.password):
        raise HTTPException(status_code=400, detail="Old password is incorrect")

    if change_data.passwd1 != change_data.passwd2:
        raise HTTPException(status_code=400, detail="New passwords do not match")

    current_user.password = get_password_hash(change_data.passwd1)
    db.add(current_user)
    db.commit()
    db.refresh(current_user)

    return {"message": "Password changed successfully"}