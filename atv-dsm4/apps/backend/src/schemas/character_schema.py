from pydantic import BaseModel
from typing import Optional

class CharacterSchema(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    level: int
    power: int

    class Config:
        from_attributes = True 