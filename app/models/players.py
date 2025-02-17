from pydantic import BaseModel

class Player(BaseModel):
    name: str
    link: str
    playerID: str
    position: str
    club: str
    age: str
    nationality: str