import secrets
from fastapi import APIRouter, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from db.session import get_db
from models.oauth_client import OAuthClient
from schemas.client import ClientCreate

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.post("/register_client/", response_model=ClientCreate)
def register_client(
    name: str = Form(...),
    client_type: str = Form(...),
    authorization_grant_type: str = Form(...),
    redirect_uris: str = Form(""),
    algorithm: str = Form(...),
    db: Session = Depends(get_db)
):
    client_id = secrets.token_urlsafe(32)
    client_secret = secrets.token_urlsafe(64)

    client = ClientCreate(
        client_id=client_id,
        client_secret=client_secret,
        name=name,
        client_type=client_type,
        authorization_grant_type=authorization_grant_type,
        redirect_uris=redirect_uris,
        algorithm=algorithm
    )

    db_client = OAuthClient(
        client_id=client.client_id,
        client_secret=client.client_secret,
        name=client.name,
        client_type=client.client_type,
        authorization_grant_type=client.authorization_grant_type,
        redirect_uris=client.redirect_uris,
        algorithm=client.algorithm,
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.post("/register_client_web/", response_class=HTMLResponse)
async def register_client_web(
    request: Request,
    name: str = Form(...),
    client_type: str = Form(...),
    authorization_grant_type: str = Form(...),
    redirect_uris: str = Form(""),
    algorithm: str = Form(...)
):
    # Validaciones básicas
    if client_type not in ["Confidential", "Public"]:
        return templates.TemplateResponse("register_client.html", {"request": request, "error": "Invalid client type"})
    if authorization_grant_type not in ["Resource owner password-based", "Authorization code"]:
        return templates.TemplateResponse("register_client.html", {"request": request, "error": "Invalid authorization grant type"})
    if algorithm not in ["No OIDC support", "HS256"]:
        return templates.TemplateResponse("register_client.html", {"request": request, "error": "Invalid algorithm"})

    client_id = secrets.token_urlsafe(32)
    client_secret = secrets.token_urlsafe(64)
    db: Session = next(get_db())
    try:
        db_client = OAuthClient(
            client_id=client_id,
            client_secret=client_secret,
            name=name,
            client_type=client_type,
            authorization_grant_type=authorization_grant_type,
            redirect_uris=redirect_uris,
            algorithm=algorithm,
        )
        db.add(db_client)
        db.commit()
        db.refresh(db_client)
        return templates.TemplateResponse("register_client.html", {"request": request, "client_id": client_id, "client_secret": client_secret})
    except Exception as e:
        db.rollback()
        return templates.TemplateResponse("register_client.html", {"request": request, "error": str(e)})
