import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

def getLastPage(soup):

    lastPageElement = soup.select_one("li.tm-pagination__list-item.tm-pagination__list-item--icon-last-page a")
    
    if lastPageElement:
        return int(lastPageElement["href"].split("Spieler_page=")[-1])
    
    return 1
 

def searchPlayers(name,page):
    url  = f'https://www.transfermarkt.co.uk/schnellsuche/ergebnis/schnellsuche?query={name.replace(' ', '+')}&Spieler_page={page}'
    headers = {   
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US"
}
    
    response = requests.get(url, headers = headers)
    

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        searchResult = soup.select("td.hauptlink:not(.rechts)")
        playerStats = soup.select("td.zentriert:not(.hauptlink)")
        playerMarketValue = soup.select("td.rechts.hauptlink")

        lastPlayerPage = getLastPage(soup)

        if searchResult:
            results = []
            
            for i, result in enumerate(searchResult[:10]):
                try:
                    playerName = result.text.strip()
                    playerLink = "https://www.transfermarkt.com" + result.a["href"]
                    playerId = playerLink.split("/")[-1]
                    playerPosition = playerStats[i * 4].text.strip()
                    playerClub = playerStats[i * 4 +1].find("img")["title"]
                    playerAge = playerStats[i * 4 + 2].text.strip()
                    
                    marketValue =  playerMarketValue[i].text.strip() if i < len(playerMarketValue) else "N/A"

                    nationalityImgs = playerStats[i * 4 + 3].find_all("img")
                    playerNationality = [img["title"] for img in nationalityImgs]

                    results.append({
                        "name": playerName,
                        "position": playerPosition,
                        "club": playerClub,
                        "age": playerAge,
                        "nationalities": playerNationality,
                        "playerId": playerId,
                        "marketValue": marketValue
                    })
                except Exception as e:
                    #In case of parsing error
                    continue    
        else:
            return None
    else:
        return None

    return {"page": page,
            "lastPage":lastPlayerPage,
             "players": results}   



