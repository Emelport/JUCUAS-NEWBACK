from sqlalchemy import Column, String, Text
from db.base import Base

class OAuthClient(Base):
    __tablename__ = 'oauth_clients'

    client_id = Column(String(255), primary_key=True, index=True)  # Especifica la longitud aquí
    client_secret = Column(String(255), nullable=False)  # Especifica la longitud aquí
    name = Column(String(255), nullable=False)  # Especifica la longitud aquí
    client_type = Column(String(255), nullable=False)  # Especifica la longitud aquí
    authorization_grant_type = Column(String(255), nullable=False)  # Especifica la longitud aquí
    redirect_uris = Column(Text, nullable=True)
    algorithm = Column(String(255), nullable=False)  # Especifica la longitud aquí
