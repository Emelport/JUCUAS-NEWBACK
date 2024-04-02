from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import conn

# usuario root,contraseña Elias2001$, en localhost mysql y bd bd_prueba

app = FastAPI()

engine = create_engine(conn)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
async def root():
    return {"message": "FUNCIONANDO ..."}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
