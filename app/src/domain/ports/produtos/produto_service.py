import requests
from src.adapters.entrypoints.api.model.produto_response_model import ProdutoResponseModel

def format_produto_data(produto_data):
    # Função para reformatar os dados para o frontend
    return {
        "PROD-XPTO": produto_data["PROD-XPTO"],
        "NOME-PROD-XPTO": produto_data["NOME-PROD-XPTO"],
        "FAM-XPTO": produto_data["FAM-XPTO"],
        "GRUPO-XPTO": produto_data["GRUPO-XPTO"],
        "CANAL-XPTO": produto_data["CANAL-XPTO"],
        "TAG-XPTO": produto_data["TAG-XPTO"],
        "DATA-HORA-ATU-XPTO": f"{produto_data['DATA-ATU-XPTO']}-{produto_data['HORA-ATU-XPTO']}",
        "ANL-ATU-XPTO": produto_data["ANL-ATU-XPTO"],
    }

def get_produto(codigo_produto: int) -> ProdutoResponseModel:
    # Faz a requisição para a mock-API
    response = requests.get(f"http://localhost:8001/XPTO?codigoProduto={codigo_produto}")
    produtos = response.json().get("Result", {}).get("AREA-XPTO", {}).get("TB-PRODUTOS", [])

    # Seleciona o primeiro produto e aplica o mapeamento
    if not produtos:
        raise ValueError("Nenhum produto encontrado para o código fornecido.")
    produto = format_produto_data(produtos[0])

    # Retorna o produto no modelo ProdutoResponseModel
    return ProdutoResponseModel(**produto)
