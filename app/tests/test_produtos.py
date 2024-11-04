from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app

client = TestClient(app)


# Teste do endpoint GET /produtos/{codigoProduto}
def test_get_produto():
    codigoProduto = "13000"
    mocked_response = {
        "codigoProduto": "13000",
        "descricao": "Descrição mockada do produto"
    }

    with patch(
        "src.domain.ports.produtos.produto_service.ProdutoService."
        "fetch_product_data"
    ) as mock_fetch:
        mock_fetch.return_value = mocked_response
        # Retorna o mock quando chamado

        # Faz a chamada para o endpoint de teste
        response = client.get(f"/produtos/{codigoProduto}")

        assert response.status_code == 200
        assert response.json() == mocked_response
