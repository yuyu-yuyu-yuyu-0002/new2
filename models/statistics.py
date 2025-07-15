from pydantic import BaseModel

class Statistics(BaseModel):
    id: int
    type: str
    count: int
