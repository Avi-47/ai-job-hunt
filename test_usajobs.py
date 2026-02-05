import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://data.usajobs.gov/api/search"

headers = {
    "Authorization-Key":os.getenv("USAJOBS_API_KEY"),
    "User-Agent":os.getenv("USAJOBS_EMAIL")
}
params = {
    "Keyword":"python developer",
    "ResultsPerPage": 3
}

response = requests.get(url, headers=headers, params=params)
if response.status_code==200:
    data=response.json()
    jobs=data["SearchResult"]["SearchResultItems"]
    for job in jobs:
        print("Title",job["MatchedObjectDescriptor"]["PositionTitle"])
        print("Location",job["MatchedObjectDescriptor"]["PositionLocation"][0]["LocationName"])
        print("-",40)
else:
    print("Error", response.status_coode, response.text)