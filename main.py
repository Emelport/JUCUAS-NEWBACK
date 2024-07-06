from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.user import router as user_router  # Asegúrate de importar el enrutador correctamente
from api.routes.universities import router as university_router  # Asegúrate de importar el enrutador correctamente
from db.base import Base  # Asegúrate de importar esto
from db.session import engine  # Asegúrate de importar el engine

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
app.include_router(university_router, prefix="/universities", tags=["Universities"])

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

