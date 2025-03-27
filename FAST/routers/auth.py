from fastapi.responses import JSONResponse
from modelsPydantic import  modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from fastapi import APIRouter


routerAuth = APIRouter()

# Endpoint Autenticacion
@routerAuth.post('/auth',tags=['Autentificación'])
def login(autorizacion:modeloAuth):
    if autorizacion.correo == 'mariano@example.com' and autorizacion.passw == '123456789':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return{"Aviso": "Usuario no autorizado"}