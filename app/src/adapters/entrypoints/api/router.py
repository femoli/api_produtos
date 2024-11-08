from fastapi import APIRouter, HTTPException
from src.domain.ports.produtos.produto_service import get_produto
from src.adapters.entrypoints.api.model.produto_response_model import ProdutoResponseModel

router = APIRouter()

@router.get("/produtos/{codigo_produto}", response_model=ProdutoResponseModel)
async def read_produto(codigo_produto: int):
    try:
        produto = get_produto(codigo_produto)
        return produto
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
