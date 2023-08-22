from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Item(str, Enum):
    indian ="indian"
    chinese = "chinese"
    italian = "italian"
    american = "american"
    
food_items = {
    1: {"name": "Cheeseburger"},
    2: {"name": "Fries"},
    3: {"name": "Milkshake"},
}

@app.get("/")
async def root():
    return "Hello World!"

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{name}")
async def get_user(name: str):
    return {"user_name": name}

# @app.get("/foods/{food_id}")
# async def get_food(food_id: int):
#     return food_items.get(food_id, {"name": "Not Found"})

@app.get("/foods/{food_type}")
async def get_food(food_type: Item):
    return {"food_type": food_type}

cupon_codes = {
    1: {"code": "abc123" , "discount": "10%"},
    2: {"code": "xyz789" , "discount": "20%"},
    3: {"code": "pqr456" , "discount": "30%"},
}

@app.get("/cupons/{cupon_id}")
async def get_cupon(cupon_id: int):
    return cupon_codes.get(cupon_id, {"code": "Not Found"})
