import pytest
from httpx import AsyncClient
from lambda_function import app


@pytest.mark.asyncio
async def test_lista_produto():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/produtos/54321")

    assert response.status_code == 200
    assert response.json() == {"nome": "Produto 1"}
