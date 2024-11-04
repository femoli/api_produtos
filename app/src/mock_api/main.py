from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

data = {
    "Data": (
        "{\"DATA-01\": {\"TABELA-PRODUTOS\":[{\"COD-PROD\":48022,"
        "\"GRUPO-PROD\":1,\"FAM-PROD\":1},{\"COD-PROD\":39847,"
        "\"GRUPO-PROD\":8,\"FAM-PROD\":7},{\"COD-PROD\":96854,"
        "\"GRUPO-PROD\":10,\"FAM-PROD\":1},{\"COD-PROD\":13116,"
        "\"GRUPO-PROD\":7,\"FAM-PROD\":2},{\"COD-PROD\":90117,"
        "\"GRUPO-PROD\":6,\"FAM-PROD\":9},{\"COD-PROD\":62050,"
        "\"GRUPO-PROD\":1,\"FAM-PROD\":9},{\"COD-PROD\":49036,"
        "\"GRUPO-PROD\":5,\"FAM-PROD\":7},{\"COD-PROD\":79034,"
        "\"GRUPO-PROD\":3,\"FAM-PROD\":5},{\"COD-PROD\":59462,"
        "\"GRUPO-PROD\":10,\"FAM-PROD\":4},{\"COD-PROD\":18776,"
        "\"GRUPO-PROD\":8,\"FAM-PROD\":3},{\"COD-PROD\":77115,"
        "\"GRUPO-PROD\":6,\"FAM-PROD\":6},{\"COD-PROD\":73905,"
        "\"GRUPO-PROD\":9,\"FAM-PROD\":4},{\"COD-PROD\":93883,"
        "\"GRUPO-PROD\":1,\"FAM-PROD\":6},{\"COD-PROD\":22196,"
        "\"GRUPO-PROD\":10,\"FAM-PROD\":7},{\"COD-PROD\":29346,"
        "\"GRUPO-PROD\":3,\"FAM-PROD\":3},{\"COD-PROD\":95170,"
        "\"GRUPO-PROD\":2,\"FAM-PROD\":1},{\"COD-PROD\":92851,"
        "\"GRUPO-PROD\":5,\"FAM-PROD\":5},{\"COD-PROD\":68073,"
        "\"GRUPO-PROD\":2,\"FAM-PROD\":8},{\"COD-PROD\":29073,"
        "\"GRUPO-PROD\":2,\"FAM-PROD\":7},{\"COD-PROD\":97595,"
        "\"GRUPO-PROD\":5,\"FAM-PROD\":7},{\"COD-PROD\":38851,"
        "\"GRUPO-PROD\":10,\"FAM-PROD\":5},{\"COD-PROD\":81852,"
        "\"GRUPO-PROD\":5,\"FAM-PROD\":5},{\"COD-PROD\":22195,"
        "\"GRUPO-PROD\":9,\"FAM-PROD\":6},{\"COD-PROD\":65063,"
        "\"GRUPO-PROD\":4,\"FAM-PROD\":10},{\"COD-PROD\":40297,"
        "\"GRUPO-PROD\":8,\"FAM-PROD\":9},{\"COD-PROD\":43124,"
        "\"GRUPO-PROD\":1,\"FAM-PROD\":2},{\"COD-PROD\":29579,"
        "\"GRUPO-PROD\":7,\"FAM-PROD\":2},{\"COD-PROD\":23057,"
        "\"GRUPO-PROD\":10,\"FAM-PROD\":1},{\"COD-PROD\":20735,"
        "\"GRUPO-PROD\":3,\"FAM-PROD\":1},{\"COD-PROD\":94805,"
        "\"GRUPO-PROD\":3,\"FAM-PROD\":2},{\"COD-PROD\":70982,"
        "\"GRUPO-PROD\":2,\"FAM-PROD\":8},{\"COD-PROD\":85879,"
        "\"GRUPO-PROD\":8,\"FAM-PROD\":10},{\"COD-PROD\":99646,"
        "\"GRUPO-PROD\":4,\"FAM-PROD\":7},{\"COD-PROD\":28555,"
        "\"GRUPO-PROD\":2,\"FAM-PROD\":3},{\"COD-PROD\":74631,"
        "\"GRUPO-PROD\":3,\"FAM-PROD\":5},{\"COD-PROD\":63125,"
        "\"GRUPO-PROD\":7,\"FAM-PROD\":10},{\"COD-PROD\":22433,"
        "\"GRUPO-PROD\":10,\"FAM-PROD\":4},{\"COD-PROD\":89375,"
        "\"GRUPO-PROD\":2,\"FAM-PROD\":8},{\"COD-PROD\":84000,"
        "\"GRUPO-PROD\":5,\"FAM-PROD\":6},{\"COD-PROD\":45930,"
        "\"GRUPO-PROD\":8,\"FAM-PROD\":9},{\"COD-PROD\":11933,"
        "\"GRUPO-PROD\":3,\"FAM-PROD\":3},{\"COD-PROD\":76674,"
        "\"GRUPO-PROD\":4,\"FAM-PROD\":3},{\"COD-PROD\":19579,"
        "\"GRUPO-PROD\":1,\"FAM-PROD\":10},{\"COD-PROD\":91934,"
        "\"GRUPO-PROD\":5,\"FAM-PROD\":6},{\"COD-PROD\":61114,"
        "\"GRUPO-PROD\":8,\"FAM-PROD\":8},{\"COD-PROD\":67534,"
        "\"GRUPO-PROD\":2,\"FAM-PROD\":2},{\"COD-PROD\":84298,"
        "\"GRUPO-PROD\":4,\"FAM-PROD\":5},{\"COD-PROD\":25407,"
        "\"GRUPO-PROD\":10,\"FAM-PROD\":3},{\"COD-PROD\":63078,"
        "\"GRUPO-PROD\":8,\"FAM-PROD\":1},{\"COD-PROD\":24034,"
        "\"GRUPO-PROD\":7,\"FAM-PROD\":9}]}}"
    )
}


@app.get("/XPTO")
async def xpto():
    return JSONResponse(content=data)
