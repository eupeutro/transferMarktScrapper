from fastapi import APIRouter, HTTPException, Query
from app.services import getPlayer

router = APIRouter()

@router.get("/")
def get_players(
    name: str = Query(..., description="Player name for search"),
    page: int = Query(1, description="Page number for search results")):
    """
    Endpoint for search players by their name.
    Example: /players?name=Pedro
    """

    playersData = getPlayer.searchPlayers(name,page)

    if playersData is None:
        raise HTTPException(status_code=404, detail="Player not found or request error")
    return playersData