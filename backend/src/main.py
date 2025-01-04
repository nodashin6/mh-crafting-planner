from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import (
    item_router,
    recipe_router,
    mixer_router,
    procurement_plan_router,
    shipment_plan_router,
)

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(item_router.router, prefix="/api")
app.include_router(recipe_router.router, prefix="/api")
app.include_router(mixer_router.router, prefix="/api")
app.include_router(procurement_plan_router.router, prefix="/api")
app.include_router(shipment_plan_router.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the MH Crafting Planner Backend"}
