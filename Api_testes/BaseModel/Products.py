from pydantic import BaseModel

class Product(BaseModel):
    nome: str
    preco: int
    descricao: str
    quantidade: int
    