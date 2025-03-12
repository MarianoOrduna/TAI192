from pydantic import BaseModel,Field
#modelo de validaciones 
class modeloUsuario(BaseModel):
    NoLicencia: str = Field(..., max_length=12,description="Solo letras min:3 max:85")
    nombre: str = Field(...,min_length=3,description="Solo letras min:3")
    tipoLicencia: str = Field(...,min_length=1,description="Solo letras A,B,C,D")
    