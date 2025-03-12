from fastapi import FastAPI 
from fastapi import FastAPI
from typing import Optional
from fastapi import FastAPI, HTTPException
from models import modeloUsuario

app = FastAPI()
app = FastAPI(
    title = 'Mi PrimerAPI 192',
    description = 'Mariano',
    version = '1.0.1'
)

#endopoint home
usuarios = [
    {"NoLicencia": 1, "Nombre": "Mario", "Tipo Licencia": 'A'},
    {"NoLicencia": 2, "Nombre": "Gelipe", "Tipo Licencia": 'B'},
    {"NoLicencia": 3, "Nombre": "Alonso", "Tipo Licencia": 'C'},
    {"NoLicencia": 4, "Nombre": "Mariano", "Tipo Licencia": 'D'}
]

@app.get("/")


@app.get('/', tags=['Hola Mundo'])
def home():
    return{"hellow":"word FastAPI"}
  
#End point ver usuarios
@app.get("/consultarUsuarios", tags=['Operaciones CRUD'])
def consultarUsuarios():
    return{'Las tareas son':usuarios}


@app.get("/usuario/", tags=["Parametro Opcional"])
def consultausuario(NoLicencia: Optional[int] = None):
    if NoLicencia is not None:
        for usu in usuarios:
            if usu["NoLicencia"] == NoLicencia:
                return {"mensaje": "Usuario encontrado", "usuario": usu}
        
        return {"mensaje": f"No se encontró el usuario con id: {NoLicencia}"}
    else :
        return {"mensaje": "No se proporcionó un id"}
    
    #Crear un nuevo conductor
@app.post('/agregarConductor/',response_model= modeloUsuario,tags=['operaciones CRUD'])
def agregarConductor(usuario:modeloUsuario):
    for usr in usuarios:
        if usr ['NoLicencia']== usuario.NoLicencia:
            raise HTTPException(status_code=400, detail='El NoLicencia ya existente')
    usuarios.append(usuario)   
    return usuario

#Endpoint para actualizar un usuario
@app.put('/usuarios/{NoLicencia}',response_model= modeloUsuario,tags=['Operaciones CRUD'])
def actualizar(NoLicencia:int,conductorActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr['NoLicencia'] == NoLicencia:
            usuarios[index]= conductorActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail='El usuario no existe')
