from src.domain.ports.produtos.produto_service import ProdutoService


async def get_product(codigoProduto: str):
    produto_service = ProdutoService()
    produto_data = await produto_service.fetch_product_data(codigoProduto)
    return produto_data
