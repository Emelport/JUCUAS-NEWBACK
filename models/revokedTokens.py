# models/revoked_token.py
from sqlalchemy import Column, String
from db.base import Base


class RevokedToken(Base):
    __tablename__ = "revoked_tokens"
    token = Column(String(255), primary_key=True, index=True)  # Especifica la longitud aquí
