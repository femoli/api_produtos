from fastapi import FastAPI, APIRouter, HTTPException
from mangum import Mangum  # Para integrar o FastAPI com AWS Lambda
import requests
import json
from typing import Dict, Any

# Importando a configuração
from src.config.settings import settings

# Instanciando o FastAPI
app = FastAPI()

# Router do produto, com um endpoint para buscar o produto por código
router = APIRouter()

# Função para desserializar os dados
def desserializar_resposta_api(serialized_data: str) -> Dict[str, Any]:
    try:
        data = json.loads(serialized_data)
        return data
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Erro ao desserializar dados: {e}")

# Função para obter dados da API
def obter_dados_da_api() -> str:
    try:
        response = requests.get(settings.BASE_URL_MAINFRAME)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro na requisição: {e}")

# Função para mapear os dados do produto
def map_produto_para_resposta_api(produto: Dict[str, Any]) -> Dict[str, Any]:
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

# Endpoint para buscar o produto por código
@router.get("/produtos/{codigo_produto}")
async def obter_produto_por_codigo(codigo_produto: int) -> Dict[str, Any]:
    serialized_data = obter_dados_da_api()  # Obtendo dados da mock API
    dados = desserializar_resposta_api(serialized_data)  # Desserializando os dados

    # Acessando os produtos
    produtos = dados.get("Result", {}).get("AREA-XPTO", {}).get("TB-PRODUTOS", [])
    
    # Buscando o produto específico
    for produto in produtos:
        if produto.get("PROD-XPTO") == codigo_produto:
            return map_produto_para_resposta_api(produto)

    raise HTTPException(status_code=404, detail="Produto não encontrado")

# Incluindo o router no app
app.include_router(router)

# Instanciando o handler do AWS Lambda
handler = Mangum(app)
