class ProdutoService:
    @staticmethod
    async def fetch_product_data(codigoProduto: str):
        # Mock de resposta
        return {
            "codigoProduto": codigoProduto,
            "descricao": "Descrição mockada do produto"
        }
