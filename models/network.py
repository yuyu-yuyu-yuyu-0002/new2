from pydantic import BaseModel

class Network(BaseModel):
    id: int
    user_id: int
    connections: int
