from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuario import routerUsuario
from routers.auth import routerAuth

app = FastAPI(
    title='My FastAPI 192', 
    description='API de Mariano',
    version='1.0.1',
)

app.include_router(routerUsuario)

Base.metadata.create_all(bind=engine)


# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

app.include_router(routerAuth)
