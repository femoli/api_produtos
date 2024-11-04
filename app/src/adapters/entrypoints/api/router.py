from fastapi import APIRouter

from src.adapters.entrypoints.api.request import get_produto_request
from src.domain.ports.produtos.produto_service import get_produto

router = APIRouter()


@router.get("/produtos/{codigoProduto}",
            response_model=get_produto_request.ProdutoResponse)
async def lista_produto(codigoProduto: int):
    return await get_produto(codigoProduto)


@router.patch("/produtos/{codigoProduto}")
async def atualiza_produto(codigoProduto: int, produto_data: dict):
    # Implementar lógica para atualizar o produto
    return {"message": "Produto atualizado com sucesso"}


@router.get("/familiaProdutos/")
async def lista_familia_produtos():
    # Implementar lógica para retornar famílias de produtos
    return []


@router.get("/generoProdutos/")
async def lista_agrupamento_produtos():
    # Implementar lógica para retornar agrupamentos de produtos
    return []
