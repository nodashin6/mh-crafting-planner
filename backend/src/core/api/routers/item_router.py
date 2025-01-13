from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from ..models.item import Item

router = APIRouter()

items = []

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.item_code == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for i, existing_item in enumerate(items):
        if existing_item.item_code == item_id:
            items[i] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.item_code == item_id:
            del items[i]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/items/", response_model=List[Item])
def list_items():
    return items
