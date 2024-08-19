from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: str
    nome: str
    preco: int
    descricao: str
    quantidade: int
