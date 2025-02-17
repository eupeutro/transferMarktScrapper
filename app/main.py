from fastapi import FastAPI
from app.routes import players

app = FastAPI()

app.include_router(players.router, prefix="/players",tags=["players"])