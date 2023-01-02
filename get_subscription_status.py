#!/usr/bin/env python3
import requests
import json
import os

API_FOOTBALL_ENDPOINT = "https://v3.football.api-sports.io"
API_FOOTBALL_HEADERS = {
	"X-RapidAPI-Key": os.environ['API_FOOTBALL_API_KEY'],
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", API_FOOTBALL_ENDPOINT + "/status", headers=API_FOOTBALL_HEADERS)
print(str(json.dumps(json.loads(response.text), indent=4)))
