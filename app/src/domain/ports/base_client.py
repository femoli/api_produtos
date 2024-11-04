class BaseClientMock:
    def obter_dados_produto(self, codigoProduto: int):
        # Retorna um mock de produto baseado no código do produto
        produtos_mock = {
            54321: {"nome": "Produto 1"},
            98765: {"nome": "Produto 2"},
        }
        return produtos_mock.get(codigoProduto,
                                 {"erro": "Produto não encontrado"})
