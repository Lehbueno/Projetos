from pydantic import BaseModel

class UserResponse(BaseModel):
    id: str
    nome: str
    email: str
    password: str
    administrador: str

    class Config:
        fields = {
            'id': '_id'
        }
