from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    text:str = None
    is_done:bool = False

@app.get("/")
def root():
    return {"Hello" : "World"}


@app.post("/items")
def create_item(item:Item):
    items.append(item)
    print(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id:int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not present")    
