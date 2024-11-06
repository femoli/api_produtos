import requests
from src.config.settings import settings

class ProdutoService:
    def __init__(self):
        self.base_url = settings.BASE_URL_MAINFRAME

    def get_produto_by_codigo(self, codigo_produto: int):
        response = requests.get(self.base_url)
        response_data = response.json()
        
        produtos = response_data["Result"]["AREA-XPTO"]["TB-PRODUTOS"]
        
        # Filtra o produto com o código especificado
        produto = next(
            (item for item in produtos if item["PROD-XPTO"] == codigo_produto), 
            None)
        return produto
