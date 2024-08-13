# schemas/client.py
from pydantic import BaseModel, Field

class ClientCreate(BaseModel):
    name: str
    client_id: str = Field(default=None)
    client_secret: str = Field(default=None)
    client_type: str
    authorization_grant_type: str
    redirect_uris: str
    algorithm: str
