from pydantic import BaseModel
from typing import Optional

class EnemySchema(BaseModel):
    id: Optional[int] = None
    name: str
    type: str
    health: int
    attack: int
    defense: int

    class Config:
        from_attributes = True 