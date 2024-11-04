from src.domain.ports.base_client import BaseClientMock
from src.domain.ports.produtos.models.produto import Produto


async def get_produto(codigoProduto: int) -> Produto:
    client = BaseClientMock()
    response = client.obter_dados_produto(codigoProduto)
    return Produto(**response)
