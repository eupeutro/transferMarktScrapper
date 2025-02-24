from fastapi import FastAPI
from app.routes import Players

app = FastAPI(
    title="transferMarktScrapper"
)

app.include_router(Players.router, prefix="/players",tags=["players"])