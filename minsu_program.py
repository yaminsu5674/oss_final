from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
app = FastAPI()


buyers = []
products = []
record_list = []


@app.exception_handler(RequestValidationError)
async def handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"result": "Error"}),
    )


@app.post("/buyers")
async def add_buyers(name: str):
    if type(name) == str:
        if name in buyers:
            return {"result": "Duplicate entry."}
        buyers.append(name)
        record_list.append({})
        return {"result": "OK"}


@app.post("/products")
async def add_products(name: str):
    if type(name) == str:
        if name in products:
            return {"result": "Duplicate entry."}
        products.append(name)
        return {"result": "OK"}


@app.post("/buyers/{buyer_name}")
async def purchase(buyer_name: str, prod_name: str):
    if not(buyer_name in buyers):
        return {"result": f"Error: no buyer {buyer_name}"}
    if not (prod_name in products):
        return {"result": f"Error: no product {buyer_name}"}
    i = buyers.index(buyer_name)
    if prod_name in record_list[i]:
        n = record_list[i][prod_name]
        record_list[i][prod_name] = n+1
    else:
        record_list[i][prod_name] = 1

    return {"result": "OK"}


@app.get("/buyers/{buyer_name}/purchased")
async def record(buyer_name: str):
    if not(buyer_name in buyers):
        return {"result": f"Error: no buyer {buyer_name}"}

    i = buyers.index(buyer_name)
    return record_list[i]


@app.get("/buyers")
async def get_buyers():
    return buyers  # as a list


@app.get("/products")
async def get_products():
    return products  # as a list
