from pydantic import BaseModel
from typing import Optional

class GameSchema(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True