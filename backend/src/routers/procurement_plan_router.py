from fastapi import APIRouter, HTTPException
from typing import List
from ..models.procurement_plan import ProcurementPlan

router = APIRouter()

procurement_plans = []

@router.post("/procurement_plans/", response_model=ProcurementPlan)
def create_procurement_plan(procurement_plan: ProcurementPlan):
    procurement_plans.append(procurement_plan)
    return procurement_plan

@router.get("/procurement_plans/{plan_id}", response_model=ProcurementPlan)
def read_procurement_plan(plan_id: int):
    for plan in procurement_plans:
        if plan.id == plan_id:
            return plan
    raise HTTPException(status_code=404, detail="Procurement plan not found")

@router.put("/procurement_plans/{plan_id}", response_model=ProcurementPlan)
def update_procurement_plan(plan_id: int, procurement_plan: ProcurementPlan):
    for i, existing_plan in enumerate(procurement_plans):
        if existing_plan.id == plan_id:
            procurement_plans[i] = procurement_plan
            return procurement_plan
    raise HTTPException(status_code=404, detail="Procurement plan not found")

@router.delete("/procurement_plans/{plan_id}")
def delete_procurement_plan(plan_id: int):
    for i, plan in enumerate(procurement_plans):
        if plan.id == plan_id:
            del procurement_plans[i]
            return {"detail": "Procurement plan deleted"}
    raise HTTPException(status_code=404, detail="Procurement plan not found")

@router.get("/procurement_plans/", response_model=List[ProcurementPlan])
def list_procurement_plans():
    return procurement_plans
