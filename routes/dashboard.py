from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard/ping")
def ping():
    return {"msg": "dashboard route ok"}
