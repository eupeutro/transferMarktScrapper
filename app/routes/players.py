from fastapi import APIRouter, HTTPException, Query
from app.services import searchPlayers

router = APIRouter()

@router.get("/")
def search_players(
    query: str = Query(..., description="Player name for search"),
    page: int = Query(1, description="Page number for search results")):
    """
    Endpoint for search players by their name.
    Example: /players?name=Pedro
    
    """

    playersData = searchPlayers.searchPlayers(query,page)

    if playersData is None:
        raise HTTPException(status_code=404, detail="Player not found or request error")
    return playersData