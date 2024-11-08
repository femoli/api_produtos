from pydantic import BaseModel, Field

class ProdutoResponse(BaseModel):
    produto_id: int = Field(..., alias="PROD-XPTO")
    familia_id: int = Field(..., alias="FAM-XPTO")
    canal_id: int = Field(..., alias="CANAL-XPTO")
    grupo_id: int = Field(..., alias="GRUPO-XPTO")
    tag: str = Field(..., alias="TAG-XPTO")
    data_atualizacao: str = Field(..., alias="DATA-ATU-XPTO")
    hora_atualizacao: str = Field(..., alias="HORA-ATU-XPTO")
    codigo_analista: str = Field(..., alias="ANL-ATU-XPTO")
    nome_produto: str = Field(..., alias="NOME-PROD-XPTO")
    
    class Config:
        allow_population_by_field_name = True
