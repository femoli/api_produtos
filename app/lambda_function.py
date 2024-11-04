import json
import requests

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


def get_produto_from_mock_api(codigo_produto: int):
    try:
        response = requests.get("http://localhost:8001/XPTO")
        response.raise_for_status()
        data = response.json()

        # Desserializar o conteúdo de "Data" como JSON
        data = json.loads(data["Data"])

        # Navegar até "TABELA-PRODUTOS" dentro de "DATA-01"
        produtos = data.get("DATA-01", {}).get("TABELA-PRODUTOS", [])
        produto = next(
            (item for item in produtos if item["COD-PROD"] == codigo_produto),
            None,
        )

        if produto is None:
            raise HTTPException(
                status_code=404,
                detail="Produto não encontrado na mock API",
            )

        return produto

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao conectar à mock API",
        ) from e
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="Erro ao processar a resposta da mock API",
        )


@app.get("/produtos/{codigo_produto}")
def get_produto(codigo_produto: int):
    produto = get_produto_from_mock_api(codigo_produto)
    return JSONResponse(content=produto)
