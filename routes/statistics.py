from fastapi import APIRouter

router = APIRouter()

@router.get("/statistics/ping")
def ping():
    return {"msg": "statistics route ok"}
