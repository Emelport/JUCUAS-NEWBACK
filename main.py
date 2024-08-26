#FastApi
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# SQLAlchemy
from db.base import Base  # Asegúrate de importar esto
from db.session import engine  # Asegúrate de importar el engine

# Configuración
from core.config import openapi_schema, origins

# Routers
from api.routes.auth import router as auth_router
from api.routes.user import router as user_router
from api.routes.universities import router as university_router
from api.routes.organizationalUnit import router as organizationalUnit_router
from api.routes.reviewers import router as reviewers_router
from api.routes.representative import router as representative_router
from api.routes.presenter import router as presenter_router
from api.routes.deadline import router as deadline_router
from api.routes.activity import router as activity_router
from api.routes.typeActivities import router as typeActivities_router
from api.routes.typeEvidence import router as typeEvidence_router
from api.routes.client import router as client_router

# Crear la aplicación
app = FastAPI()

# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     # Registrar la solicitud
#     print(f"Request: {request.method} {request.url}")
#     response = await call_next(request)
#     return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir routers
#NOTA: A como se vayan agregando las rutas se van creando las tablas en la base de datos
app.include_router(university_router, prefix="/university", tags=["University"])
app.include_router(organizationalUnit_router, prefix="/organizational-unit", tags=["OrganizationalUnit"])
app.include_router(reviewers_router, prefix="/reviewer", tags=["Reviewers"])
app.include_router(representative_router, prefix="/representative", tags=["Representative"])
app.include_router(presenter_router, prefix="/presenter", tags=["Presenter"])
app.include_router(deadline_router, prefix="/deadline", tags=["Deadline"])
app.include_router(activity_router, prefix="/activity", tags=["Activities"])
app.include_router(typeActivities_router, prefix="/typeActivity", tags=["TypeActivities"])
app.include_router(typeEvidence_router, prefix="/typeEvidences", tags=["TypeEvidences"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(client_router, prefix="/clients", tags=["oAuth Clients"])
app.include_router(user_router, prefix="/users", tags=["Users"])



templates = Jinja2Templates(directory="templates")


# Function para crear las tablas en la base de datos al inicio
@app.on_event("startup")
def on_startup():
    # Crear las tablas en la base de datos
    Base.metadata.create_all(bind=engine)

# Ruta para Registrar una application cliente
@app.get("/", response_class=HTMLResponse)
async def get_register_form(request: Request):
    return templates.TemplateResponse("register_client.html", {"request": request})


# Ejecutar la aplicación usando Uvicorn si se ejecuta directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
