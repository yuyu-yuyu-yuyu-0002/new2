from pydantic import BaseModel

class Analytics(BaseModel):
    id: int
    metric: str
    value: float
