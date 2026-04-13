from pydantic import BaseModel

class LevelSchema(BaseModel):
    id: int
    game_id: int
    title: str
    order: int