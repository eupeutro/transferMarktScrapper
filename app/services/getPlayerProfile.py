import requests
from bs4 import BeautifulSoup

def getPlayerProfile(playerID):
    url = f'https://www.transfermarkt.co.uk/default/profil/spieler/{playerID}'
    headers = {   
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US"
}
    
    response = requests.get(url, headers = headers)

    if response.status_code ==  200:
        soup = BeautifulSoup(response.text, "html.parser")
        result = []

        playerInfo= soup.select("span.info-table__content--bold")
        
        #print(playerInfo) 
        try :
                playerName = playerInfo[0].text.strip()
                playerBirthDate = playerInfo[1].text.strip()
                playerBirthPlace = playerInfo[2].text.strip()
                playerHeight = playerInfo[3].text.strip()
                playerNationality = playerInfo[4].text.strip()
                playerPosition = playerInfo[5].text.strip()
                playerStrongFoot = playerInfo[6].text.strip()
                playerCurrentClub = playerInfo[8].text.strip()
                joinedAtClub = playerInfo[9].text.strip()
                contractExpiration = playerInfo[10].text.strip()


                result.append({
                     "fullName":playerName,
                     "birthDate":playerBirthDate,
                     "birthPlace":playerBirthPlace,
                     "height":playerHeight,
                     "nationality": playerNationality,
                     "position": playerPosition,
                     "strongFoot": playerStrongFoot,
                     "currentClub": playerCurrentClub,
                     "joinedAtClub": joinedAtClub,
                     "contractExpiration": contractExpiration

                })

                print(result)
        except Exception as e:
            print("error")

id = 102017
getPlayerProfile(id)