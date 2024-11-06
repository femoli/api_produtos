from fastapi import APIRouter, HTTPException
from src.domain.ports.produtos.produto_service import ProdutoService

router = APIRouter()
produto_service = ProdutoService()

@router.get("/produtos/{codigoProduto}")
async def get_produto(codigoProduto: int):
    produto = produto_service.get_produto_by_codigo(codigoProduto)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto
