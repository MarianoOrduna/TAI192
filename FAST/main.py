from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title = 'Mi PrimerAPI 192',
    description = 'Bernal',
    version = '1.0.1'
)

usuarios = [
    {"id": 1, "Nombre": "Mario", "Edad": 21},
    {"id": 2, "Nombre": "Gelipe", "Edad": 20},
    {"id": 3, "Nombre": "Alonso", "Edad": 22},
    {"id": 4, "Nombre": "Mariano", "Edad": 23}
]


# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

#endpoint promedio
@app.get('/promedio', tags=['Mi Calificacion Parcial'])
def promedio():
    return 10
    
#endpoint parametros
@app.get('/usuario/{id}', tags=['Parametro Obligatorio'])
def ConsultaUsuario(id:int):
    #conectamos a la Bd
    #consultamos
    return {'Se encontro el Usuario':id}

# Endpoint parámetro opcional
@app.get("/usuario/", tags=["Parametro Opcional"])
def consultausuario(id: Optional[int] = None):
    if id is not None:
        for usu in usuarios:
            if usu["id"] == id:
                return {"mensaje": "Usuario encontrado", "usuario": usu}
        
        return {"mensaje": f"No se encontró el usuario con id: {id}"}
    else :
        return {"mensaje": "No se proporcionó un id"}


#cd fast
#Get-ExecutionPolicy 
#.\entornofast\Scripts\activate
#uvicorn main:app --reload --port 5000
