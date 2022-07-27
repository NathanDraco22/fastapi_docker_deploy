from typing import List
from fastapi import FastAPI, Path, HTTPException

from models.item_model import ItemModel
from fakeDb.fake_db import fake_db
from models.response_model import ResponseModel

app = FastAPI(title= "Mi Servicio REST")

@app.get("/")
async def home():
    return "Bienvenido a mi Servidor FASTAPI con Docker"

@app.get("/getAll", response_model= List[ItemModel])
async def get_all_items():
    data_reponse : List[ItemModel] = []
    for data in fake_db:
        data_reponse.append(ItemModel(**data))
    return data_reponse

@app.get("/getItem/{item_id}", response_model= ItemModel)
async def get_item_by_index(item_id : int = Path(title= "Element by Index")):
    try:
        data = ItemModel(**fake_db[item_id])
        return data
    except:
        raise HTTPException(status_code= 404, detail= "Item not found")

@app.post("/createItem", response_model= ResponseModel,)
async def create_an_item(body : ItemModel):
    fake_db.append({
        "name" : body.name,
        "price" : body.price
    })
    return ResponseModel(
        ok  = True,
        msg = "Object Saved"
    )

    

