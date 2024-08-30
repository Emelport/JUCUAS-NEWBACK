import os
from dotenv import load_dotenv
from fastapi.openapi.models import OAuthFlowPassword as OAuthFlowPasswordModel
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
DATABASE_URL = os.getenv("DATABASE_URL")

conn = DATABASE_URL

user = os.getenv("user")
password = os.getenv("password")
server = os.getenv("server")
bd_name = os.getenv("bd_name")


# Configuración CORS
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
]


openapi_schema = {
    "components": {
        "securitySchemes": {
            "OAuth2PasswordBearer": {
                "type": "oauth2",
                "flows": OAuthFlowsModel(
                    password=OAuthFlowPasswordModel(
                        tokenUrl="/token"  # URL del endpoint para obtener el token
                    )
                ),
            }
        }
    },
    "security": [{"OAuth2PasswordBearer": []}],  # Requerir autenticación para todos los endpoints
}