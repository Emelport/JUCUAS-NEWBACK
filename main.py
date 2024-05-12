from fastapi import FastAPI, Cookie, Header
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

@app.get("/items")
async def read_items(cookie_id: str | None = Cookie(None),
                 accept_encoding: str | None = Header(None),
                 sec_ch_ua: str | None = Header(None),
                 user_agent: str | None = Header(None),
                 x_token: list[str] | None = Header(None)
):
    return {"cookie_id": cookie_id,
            "accept_encoding": accept_encoding,
            "sec_ch_ua": sec_ch_ua,
            "user_agent": user_agent,
            "x_token": x_token}