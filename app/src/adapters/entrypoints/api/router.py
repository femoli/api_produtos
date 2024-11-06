from fastapi import APIRouter, HTTPException
from typing import Optional
from src.domain.usecases.list_produto import obter_produto_por_codigo

router = APIRouter()

@router.get("/produtos/{codigo_produto}", response_model=dict)
async def get_produto(codigo_produto: int):
    """
    Endpoint para retornar o produto com base no código fornecido.
    
    Args:
        codigo_produto (int): Código do produto a ser consultado.

    Returns:
        dict: Dados do produto formatados.
    """
    produto = obter_produto_por_codigo(codigo_produto)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto
