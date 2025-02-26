from fastapi import FastAPI, HTTPException
from typing import Optional, List
from models import modeloUsuario

app = FastAPI(
    title='My FastAPI 192', 
    description='API de Mariano',
    version='1.0.1',
)



#BD ficticia

usuarios=[
    {"id":1,"nombre":"Jelipe","edad":20,"correo":"correo1@gmail.com"},
    {"id":2,"nombre":"Kevin","edad":23,"correo":"correo2@gmail.com"},
    {"id":3,"nombre":"Manlio","edad":26,"correo":"correo3@gmail.com"},
    {"id":4,"nombre":"Mari","edad":29,"correo":"correo4@gmail.com"}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

# Endpoint CONSULTA TODOS
@app.get('/todoUsuarios', response_model= List[modeloUsuario] ,tags=['Operaciones CRUD'])
def leerUsuarios():
    return usuarios

#endpoint agregar nuevos
@app.post('/usuario/',response_model= modeloUsuario, tags=['Operaciones CRUD'])
def agregarUsuario(usuario:modeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="ID ya existente")
    usuarios.append(usuario)
    return usuario

#enpoint actualizar usuarios
@app.put('/usuarios/{id}',response_model= modeloUsuario, tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

#endpoint Eliminar Usuario
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar(id:int,usuarioEliminado:dict):
    for usr in (usuarios):
        if usr["id"] == id:
            usuarios.remove(usr)
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