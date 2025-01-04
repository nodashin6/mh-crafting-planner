from fastapi import APIRouter, HTTPException
from typing import List
from ..models.shipment_plan import ShipmentPlan

router = APIRouter()

shipment_plans = []

@router.post("/shipment_plans/", response_model=ShipmentPlan)
def create_shipment_plan(shipment_plan: ShipmentPlan):
    shipment_plans.append(shipment_plan)
    return shipment_plan

@router.get("/shipment_plans/{plan_id}", response_model=ShipmentPlan)
def read_shipment_plan(plan_id: int):
    for plan in shipment_plans:
        if plan.id == plan_id:
            return plan
    raise HTTPException(status_code=404, detail="Shipment plan not found")

@router.put("/shipment_plans/{plan_id}", response_model=ShipmentPlan)
def update_shipment_plan(plan_id: int, shipment_plan: ShipmentPlan):
    for i, existing_plan in enumerate(shipment_plans):
        if existing_plan.id == plan_id:
            shipment_plans[i] = shipment_plan
            return shipment_plan
    raise HTTPException(status_code=404, detail="Shipment plan not found")

@router.delete("/shipment_plans/{plan_id}")
def delete_shipment_plan(plan_id: int):
    for i, plan in enumerate(shipment_plans):
        if plan.id == plan_id:
            del shipment_plans[i]
            return {"detail": "Shipment plan deleted"}
    raise HTTPException(status_code=404, detail="Shipment plan not found")

@router.get("/shipment_plans/", response_model=List[ShipmentPlan])
def list_shipment_plans():
    return shipment_plans
