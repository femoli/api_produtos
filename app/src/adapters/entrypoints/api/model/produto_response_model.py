from pydantic import BaseModel

class ProdutoResponseModel(BaseModel):
    codigo_produto: int
    nome_produto: str
    familia_produto: int
    grupo_produto: int
    canal_produto: int
    tag_produto: str
    data_hora_atu: str
    anal_atu: str

    class Config:
        # Aqui definimos os aliases para que os nomes possam ser renomeados
        fields = {
            'codigo_produto': 'PROD-XPTO',
            'nome_produto': 'NOME-PROD-XPTO',
            'familia_produto': 'FAM-XPTO',
            'grupo_produto': 'GRUPO-XPTO',
            'canal_produto': 'CANAL-XPTO',
            'tag_produto': 'TAG-XPTO',
            'data_hora_atu': 'DATA-HORA-ATU-XPTO',
            'anal_atu': 'ANL-ATU-XPTO',
        }
