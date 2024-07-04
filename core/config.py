import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
DATABASE_URL = os.getenv("DATABASE_URL")

conn = DATABASE_URL

user = os.getenv("user")
password = os.getenv("password")
server = os.getenv("server")
bd_name = os.getenv("bd_name")