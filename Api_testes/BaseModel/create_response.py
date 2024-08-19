from pydantic import BaseModel
from pydantic import BaseModel, Field

class CreateResponse(BaseModel):
    id: str = Field(..., alias='_id')
    message: str

class CreateResponse(BaseModel):
    id: str  # Correspondente ao "_id" no JSON
    message: str