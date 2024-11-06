import json
import requests
from typing import Dict, Any
from fastapi.responses import JSONResponse
from fastapi import FastAPI

app = FastAPI()

data = "{\"Result\": {\"AREA-XPTO\": {\"TB-PRODUTOS\": [{\"PROD-XPTO\": 23431, \"FAM-XPTO\": 2, \"CANAL-XPTO\": 1, \"GRUPO-XPTO\": 32, \"TAG-XPTO\": \"Y\", \"DATA-ATU-XPTO\": \"25.02.2017\", \"HORA-ATU-XPTO\": \"00:00:00\", \"ANL-ATU-XPTO\": \"654956769\", \"NOME-PROD-XPTO\": \"CLASSIC CHOCO DELIGHT\", \"DESC1-XPTO\": \"\", \"DESC2-XPTO\": \"\", \"DESC3-XPTO\": \"\", \"MSG-UPDATE-XPTO\": \"\", \"FLAG-XPTO\": \"S\"}, {\"PROD-XPTO\": 95409, \"FAM-XPTO\": 9, \"CANAL-XPTO\": 3, \"GRUPO-XPTO\": 33, \"TAG-XPTO\": \"Z\", \"DATA-ATU-XPTO\": \"22.01.2007\", \"HORA-ATU-XPTO\": \"00:00:00\", \"ANL-ATU-XPTO\": \"624092415\", \"NOME-PROD-XPTO\": \"MOCHA CARAMEL TWIST\", \"DESC1-XPTO\": \"\", \"DESC2-XPTO\": \"\", \"DESC3-XPTO\": \"\", \"MSG-UPDATE-XPTO\": \"\", \"FLAG-XPTO\": \"S\"}, {\"PROD-XPTO\": 45543, \"FAM-XPTO\": 8, \"CANAL-XPTO\": 3, \"GRUPO-XPTO\": 63, \"TAG-XPTO\": \"Y\", \"DATA-ATU-XPTO\": \"08.06.2017\", \"HORA-ATU-XPTO\": \"00:00:00\", \"ANL-ATU-XPTO\": \"669026587\", \"NOME-PROD-XPTO\": \"VANILLA ICE BLACK\", \"DESC1-XPTO\": \"\", \"DESC2-XPTO\": \"\", \"DESC3-XPTO\": \"\", \"MSG-UPDATE-XPTO\": \"\", \"FLAG-XPTO\": \"S\"}, [...] \"Server\": \"serv0123456\", \"Terminal\": \"\"}}"


def desserializar_resposta_api(serialized_data: str) -> Dict[str, Any]:
    """
    Desserializa a string JSON retornada pela mock API.

    Args:
        serialized_data (str): String JSON a ser desserializada.

    Returns:
        dict: Dados desserializados.

    Raises:
        ValueError: Se houver erro na desserialização.
    """
    try:
        data = json.loads(serialized_data)
        print(f"Dados desserializados: {data}")  # Log dos dados desserializados
        return data
    except json.JSONDecodeError as e:
        print(f"Erro ao desserializar dados: {e}")
        raise ValueError("Erro ao desserializar os dados da resposta da API") from e


def obter_dados_da_api() -> str:
    """
    Faz uma requisição HTTP para a transação configurada e obtém a resposta.

    Returns:
        str: Resposta da API como uma string JSON.

    Raises:
        ValueError: Se houver erro na requisição.
    """
    try:
        # Requisição HTTP para a mock API
        response = requests.get("http://localhost:8000/XPTO")  # Substitua com o URL da sua mock-API
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx

        print(f"Resposta da API: {response.text}")  # Log da resposta recebida

        return response.text  # Retorna a resposta como string

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        raise ValueError("Erro ao fazer a requisição para a API mockada") from e


def map_produto_para_resposta_api(produto: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mapeia os dados do produto da API para o formato que será retornado no GET.

    Args:
        produto (dict): Dados do produto obtidos da resposta da API.

    Returns:
        dict: Produto no formato final para retorno ao cliente.
    """
    return {
        "codigoProduto": produto.get("PROD-XPTO"),
        "familiaProduto": produto.get("FAM-XPTO"),
        "canalProduto": produto.get("CANAL-XPTO"),
        "grupoProduto": produto.get("GRUPO-XPTO"),
        "tagProduto": produto.get("TAG-XPTO"),
        "dataAtualizacao": produto.get("DATA-ATU-XPTO"),
        "horaAtualizacao": produto.get("HORA-ATU-XPTO"),
        "analistaAtualizacao": produto.get("ANL-ATU-XPTO"),
        "nomeProduto": produto.get("NOME-PROD-XPTO"),
        "descricaoProduto": produto.get("DESC1-XPTO") or produto.get("DESC2-XPTO") or produto.get("DESC3-XPTO"),
        "mensagemAtualizacao": produto.get("MSG-UPDATE-XPTO"),
        "flagProduto": produto.get("FLAG-XPTO")
    }


def obter_produto_por_codigo(codigo_produto: int) -> Dict[str, Any]:
    """
    Obtém os dados de um produto específico a partir da API mockada.

    Args:
        codigo_produto (int): Código do produto a ser procurado.

    Returns:
        dict: Dados do produto encontrado ou erro.
    """
    serialized_data = obter_dados_da_api()  # Obtém a string JSON

    # Verificar e desserializar a resposta
    try:
        dados = desserializar_resposta_api(serialized_data)
    except ValueError:
        return {"error": "Erro ao processar a resposta da API. Dados inválidos."}

    # Verifique a estrutura dos dados. Imprimir os dados para depuração
    print(f"Dados recebidos: {dados}")  # Log completo dos dados recebidos

    # Acessa a estrutura de dados, verificando a existência dos campos
    try:
        produtos = dados.get("Result", {}).get("AREA-XPTO", {}).get("TB-PRODUTOS", [])
    except AttributeError as e:
        return {"error": "Erro ao acessar os dados. Estrutura de resposta inesperada."}

    print(f"Produtos encontrados: {produtos}")  # Log dos produtos encontrados

    # Busca o produto pelo código
    for produto in produtos:
        print(f"Produto em iteração: {produto}")  # Log do produto sendo iterado
        if produto.get("PROD-XPTO") == codigo_produto:
            # Retorna o produto mapeado para o formato desejado
            return map_produto_para_resposta_api(produto)

    return {"error": "Produto não encontrado."}


@app.get("/XPTO")
async def xpto():
    """
    Endpoint que simula a resposta da API mockada.

    Returns:
        JSONResponse: Resposta com a string JSON da mock API.
    """
    return JSONResponse(content=data, media_type="application/json")


def exibir_produto(codigo_produto: int):
    """
    Função para exibir os dados do produto ou erro.

    Args:
        codigo_produto (int): O código do produto a ser procurado.
    """
    produto = obter_produto_por_codigo(codigo_produto)

    if "error" in produto:
        print(f"Erro: {produto['error']}")
    else:
        print(f"Produto Encontrado: {produto}")
