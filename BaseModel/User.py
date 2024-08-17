from pydantic import BaseModel

class User(BaseModel):
    nome: str
    email: str
    password: str
    administrador: str
