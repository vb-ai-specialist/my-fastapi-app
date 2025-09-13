from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

items = []

class Item(BaseModel):
    text:str
    is_done:bool = False

@app.get("/")
def root():
    return {"Hello" : "World"}


@app.post("/items", response_model=List[Item])
def create_item(item:Item):
    items.append(item)
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id:int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not present")    
