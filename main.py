from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.base import Base  # Asegúrate de importar esto
from db.session import engine  # Asegúrate de importar el engine

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


app = FastAPI()

# Configuración CORS
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

# Incluir routers
#NOTA: A como se vayan agregando las rutas se van creando las tablas en la vase de datos
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(university_router, prefix="/university", tags=["University"])
app.include_router(organizationalUnit_router, prefix="/organizational-unit", tags=["OrganizationalUnit"])
app.include_router(reviewers_router, prefix="/reviewer", tags=["Reviewers"])
app.include_router(representative_router, prefix="/representative", tags=["Representative"])
app.include_router(presenter_router, prefix="/presenter", tags=["Presenter"])
app.include_router(deadline_router, prefix="/deadline", tags=["Deadline"])
app.include_router(activity_router, prefix="/activity", tags=["activities"])
app.include_router(typeActivities_router, prefix="/typeActivity", tags=["typeActivities"])
app.include_router(typeEvidence_router, prefix="/typeEvidences", tags=["typeEvidences"])

# Función para crear las tablas en la base de datos al inicio
@app.on_event("startup")
def on_startup():
    # Crear las tablas en la base de datos
    Base.metadata.create_all(bind=engine)



# Ruta de prueba para verificar que la aplicación está funcionando
@app.get("/")
async def root():
    return {"message": "FUNCIONANDO ..."}

# Ejecutar la aplicación usando Uvicorn si se ejecuta directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

