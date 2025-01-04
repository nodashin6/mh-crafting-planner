from fastapi import APIRouter, HTTPException
from typing import List
from ..models.mixer import Mixer

router = APIRouter()

mixers = []

@router.post("/mixers/", response_model=Mixer)
def create_mixer(mixer: Mixer):
    mixers.append(mixer)
    return mixer

@router.get("/mixers/{mixer_id}", response_model=Mixer)
def read_mixer(mixer_id: int):
    for mixer in mixers:
        if mixer.id == mixer_id:
            return mixer
    raise HTTPException(status_code=404, detail="Mixer not found")

@router.put("/mixers/{mixer_id}", response_model=Mixer)
def update_mixer(mixer_id: int, mixer: Mixer):
    for i, existing_mixer in enumerate(mixers):
        if existing_mixer.id == mixer_id:
            mixers[i] = mixer
            return mixer
    raise HTTPException(status_code=404, detail="Mixer not found")

@router.delete("/mixers/{mixer_id}")
def delete_mixer(mixer_id: int):
    for i, mixer in enumerate(mixers):
        if mixer.id == mixer_id:
            del mixers[i]
            return {"detail": "Mixer deleted"}
    raise HTTPException(status_code=404, detail="Mixer not found")

@router.get("/mixers/", response_model=List[Mixer])
def list_mixers():
    return mixers
