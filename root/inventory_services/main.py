# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from inventory import InventoryManager

app = FastAPI(
    title="Inventory Service",
    description="Tracks inventory of tshirts and pants",
    version="1.0.0"
)

manager = InventoryManager()

class InventoryUpdate(BaseModel):
    item: str
    change: int

@app.get("/")
def root():
    return {"message": "Welcome to the Inventory Service! Visit /docs for API documentation."}

@app.get("/inventory")
def get_inventory():
    return manager.get_inventory()

@app.post("/inventory")
def post_inventory(update: InventoryUpdate):
    try:
        return manager.update_inventory(update.item, update.change)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
