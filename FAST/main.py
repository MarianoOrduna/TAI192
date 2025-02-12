from fastapi import FastAPI,HTTPException
from typing import Optional

app = FastAPI(
    title = 'Mi PrimerAPI 192',
    description = 'Mariano',
    version = '1.0.1'
)

usuarios = [
    {"id": 1, "Nombre": "Mario", "Edad": 21},
    {"id": 2, "Nombre": "Gelipe", "Edad": 20},
    {"id": 3, "Nombre": "Alonso", "Edad": 22},
    {"id": 4, "Nombre": "Mariano", "Edad": 23}
]



#Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}


#endpoint Consulta todos
@app.get('/todosUsuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
    return{'Los usuarios registrados son': usuarios}

#endpoint agregar nuevos
@app.post('/usuario/', tags=['Operaciones CRUD'])
def agregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="ID ya existente")
    usuarios.append(usuario)
    return usuario

#enpoint actualizar usuarios
@app.put('/usuarios/{id}',tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")


#aqui es importante agregar parametros
#En los parametros va primero el nombre y despues el tipo de dato



#endpoint promedio
#@app.get('/promedio', tags=['Mi Calificacion Parcial'])
#def promedio():
    #return 10
    
#endpoint parametros
#@app.get('/usuario/{id}', tags=['Parametro Obligatorio'])
#def ConsultaUsuario(id:int):
    #conectamos a la Bd
    #consultamos
 #   return {'Se encontro el Usuario':id}

# Endpoint parámetro opcional
#@app.get("/usuario/", tags=["Parametro Opcional"])
#def consultausuario(id: Optional[int] = None):
 #   if id is not None:
  #      for usu in usuarios:
   #         if usu["id"] == id:
    #            return {"mensaje": "Usuario encontrado", "usuario": usu}
        
     #   return {"mensaje": f"No se encontró el usuario con id: {id}"}
    #lse :
     #   return {"mensaje": "No se proporcionó un id"}


#cd fast
#Get-ExecutionPolicy 
#.\entornofast\Scripts\activate
#uvicorn main:app --reload --port 5000
#Get-ExecutionPolicy
#Set-ExecutionPolicy Unrestricted -Scope Process