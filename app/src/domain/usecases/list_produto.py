from src.domain.ports.produtos.produto_service import ProdutoService

def listar_produto_por_codigo(codigoProduto: int) -> dict:
    service = ProdutoService()
    return service.get_produto(codigoProduto)
