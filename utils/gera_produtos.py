import random
import json
from datetime import datetime, timedelta

def generate_random_product():
    # Gerar valores aleatórios para cada campo
    prod_xpto = random.randint(10000, 99999)
    fam_xpto = random.randint(1, 10)
    canal_xpto = random.randint(0, 5)
    grupo_xpto = random.randint(10, 99)
    tag_xpto = random.choice(["X", "Y", "Z"])

    # Gerar datas e horas aleatórias entre 2000 e 2023
    start_date = datetime(2000, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days))
    data_atu_xpto = random_date.strftime("%d.%m.%Y")
    hora_atu_xpto = random_date.strftime("%H:%M:%S")

    anl_atu_xpto = str(random.randint(100000000, 999999999))
    nome_prod_xpto = random.choice([
        "VANILLA ICE BLACK", "PERSONA VENICE MASTER BLASTER ITALIC",
        "CLASSIC CHOCO DELIGHT", "MOCHA CARAMEL TWIST",
        "NIGHT SHADOW SILVER", "GOLDEN SUNSET ELEGANCE"
    ])

    return {
        "PROD-XPTO": prod_xpto,
        "FAM-XPTO": fam_xpto,
        "CANAL-XPTO": canal_xpto,
        "GRUPO-XPTO": grupo_xpto,
        "TAG-XPTO": tag_xpto,
        "DATA-ATU-XPTO": data_atu_xpto,
        "HORA-ATU-XPTO": hora_atu_xpto,
        "ANL-ATU-XPTO": anl_atu_xpto,
        "NOME-PROD-XPTO": nome_prod_xpto,
        "DESC1-XPTO": "",
        "DESC2-XPTO": "",
        "DESC3-XPTO": "",
        "MSG-UPDATE-XPTO": "",
        "FLAG-XPTO": "S"
    }

# Gerar 100 produtos
products = [generate_random_product() for _ in range(100)]

# Ordenar os produtos pelo campo PROD-XPTO, do menor para o maior
products_sorted = sorted(products, key=lambda x: x["PROD-XPTO"])

# Estrutura final
final_data = {
    "Result": {
        "AREA-XPTO": {
            "TB-PRODUTOS": products_sorted
        },
        "Server": "serv0123456",
        "Terminal": ""
    }
}

# Serializar o JSON duas vezes para incluir as barras invertidas
double_serialized_json = json.dumps({"Data": json.dumps(final_data)})

# Salvar no arquivo produtos_gerados.json
with open("produtos_gerados.json", "w") as f:
    f.write(double_serialized_json)

print("Arquivo produtos_gerados.json criado com sucesso!")
