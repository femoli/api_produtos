from fastapi.testclient import TestClient
# from src.adapters.entrypoints.api.router import router
from src.main import app

client = TestClient(app)


def test_get_produto():
    codigoProduto = "13000"
    response = client.get(f"/produtos/{codigoProduto}")
    assert response.status_code == 200
    assert "codigoProduto" in response.json()
