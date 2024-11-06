from src.domain.ports.produtos.produto_service import buscar_produto_por_codigo
from typing import Dict, Any

def obter_produto_por_codigo(codigo_produto: int) -> Dict[str, Any]:
    """
    Usecase responsável por buscar um produto a partir de seu código.

    Args:
        codigo_produto (int): O código do produto.

    Returns:
        dict: Dados do produto ou um dicionário vazio caso não encontrado.
    """
    produto = buscar_produto_por_codigo(codigo_produto)
    return produto
