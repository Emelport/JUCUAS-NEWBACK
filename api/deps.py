from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from db.session import get_db
from models.users import User as SQLUser
from schemas.users import TokenData
from core.config import *
from typing import List
from sqlalchemy.orm import joinedload


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    # Utilizar joinedload para asegurarse de que los grupos se cargan
    user = db.query(SQLUser).options(joinedload(SQLUser.groups)).filter(SQLUser.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user


def oauth2_scheme_with_validation(token: str = Depends(oauth2_scheme)) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return token


def get_current_active_user(current_user: SQLUser = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def group_required(groups: List[str]):
    # Ejemplo de uso
    # @router.get("/admin-area")
    # async def admin_area(current_user: SQLUser = Depends(group_required(["admin"]))):
    #     return {"message": f"Welcome to the admin area, {current_user.username}!"}
    def user_group_dependency(current_user: SQLUser = Depends(get_current_user)):
        if not any(group.name in groups for group in current_user.groups):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operation not permitted. User does not have required group."
            )
        return current_user
    return user_group_dependency

