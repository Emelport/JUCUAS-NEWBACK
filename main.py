from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from settings import conn
from models.schema import *


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

engine = create_engine(conn)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "FUNCIONANDO ..."}

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


# ##************USERS************##
# @app.post("/users/")
# async def create_user(user: User, db: Session = Depends(get_db)):
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user
#
# @app.get("/users/")
# async def read_users(db: Session = Depends(get_db)):
#     users = db.query(User).all()
#     return [user.__dict__ for user in users]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
