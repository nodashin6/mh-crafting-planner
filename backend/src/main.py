from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core import supabase_client
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/api/v1/items")
def fetch_items():
    response = supabase_client().table("items").select("*").execute()
    return JSONResponse(content=response.data)


@app.get("/api/v1/mixers")
def fetch_mixers():
    response = supabase_client().table("mixers").select("*").execute()
    return JSONResponse(content=response.data)


@app.get("/api/v1/recipes")
def fetch_recipes():
    response = supabase_client().table("recipes").select("*").execute()
    return JSONResponse(content=response.data)

@app.get("/api/v1/markets")
def fetch_shipments():
    response = supabase_client().table("markets").select("*").execute()
    return JSONResponse(content=response.data)
