from fastapi import APIRouter, HTTPException
from typing import List
from ..models.recipe import Recipe

router = APIRouter()

recipes = []

@router.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: Recipe):
    recipes.append(recipe)
    return recipe

@router.get("/recipes/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int):
    for recipe in recipes:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.put("/recipes/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: Recipe):
    for i, existing_recipe in enumerate(recipes):
        if existing_recipe.id == recipe_id:
            recipes[i] = recipe
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    for i, recipe in enumerate(recipes):
        if recipe.id == recipe_id:
            del recipes[i]
            return {"detail": "Recipe deleted"}
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.get("/recipes/", response_model=List[Recipe])
def list_recipes():
    return recipes
