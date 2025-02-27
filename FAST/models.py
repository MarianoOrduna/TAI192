from pydantic import BaseModel, EmailStr, Field
#modelo de validaciones 
class modeloUsuario(BaseModel):
    id: int = Field(...,gt=0,description="id unico y solo numeros positivos")
    nombre: str = Field(...,min_length=3,max_length=85,description="Solo letras min:3 max:85")
    edad: int = Field(...,min_length=0,max_length=121,description="Solo letras min:0 max:121")
    correo: EmailStr = Field(..., description="Debe ser un correo electrónico válido", example="example@gmail.com")