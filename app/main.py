from fastapi import FastAPI
from app.routes import players

app = FastAPI(
    title="transferMarktScrapper"
)

app.include_router(players.router, prefix="/Players",tags=["Players"])