from fastapi import APIRouter

router = APIRouter()

@router.get("/network/ping")
def ping():
    return {"msg": "network route ok"}
