from DB.conexion import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'tbUsers'  # Uso de __tablename__ con dos guiones bajos
    id = Column(Integer, primary_key=True, autoincrement=True)  # autoincrement=True
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
