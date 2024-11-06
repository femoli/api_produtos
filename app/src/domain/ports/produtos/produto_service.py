from src.domain.ports.produtos.mappers.produto_mapper import obter_produto_por_codigo
from typing import Dict, Any

def buscar_produto_por_codigo(codigo_produto: int) -> Dict[str, Any]:
    """
    Serviço para buscar um produto pelo código, integrando com o mapeador para
    obter os dados da API e desserializar a resposta.

    Args:
        codigo_produto (int): Código do produto a ser procurado.

    Returns:
        dict: Dados do produto, ou um dicionário vazio caso não encontrado.
    """
    produto = obter_produto_por_codigo(codigo_produto)
    return produto
