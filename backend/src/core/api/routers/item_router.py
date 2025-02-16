from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from ...domain import models

router = APIRouter()

items = []


@router.post("/items/", response_model=models.Item)
def create_item(item: models.Item):
    items.append(item)
    return item


@router.get("/items/{item_id}", response_model=models.Item)
def read_item(item_id: int):
    for item in items:
        if item.item_code == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/items/{item_id}", response_model=models.Item)
def update_item(item_id: int, item: models.Item):
    for i, existing_item in enumerate(items):
        if existing_item.item_code == item_id:
            items[i] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/items/{item_id}", response_model=models.Item)
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.item_code == item_id:
            del items[i]
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")


@router.get("/items/", response_model=List[models.Item])
def list_items():
    return items
