from pydantic import BaseModel


class ProdutoResponse(BaseModel):
    nome: str
