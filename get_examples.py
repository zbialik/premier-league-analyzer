#!/usr/bin/env python3
import requests
import json
import os

API_FOOTBALL_ENDPOINT = "https://v3.football.api-sports.io"
API_FOOTBALL_HEADERS = {
	"X-RapidAPI-Key": os.environ['API_FOOTBALL_API_KEY'],
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

API_FOOTBALL_PREMIER_LEAGUE_ID = 39 # retrieved from dashboard
API_FOOTBALL_CURRENT_SEASON = 2022

playerId = 19959 # Ben White
fixtureId = 868117 # Brighton vs Arsenal on Dec 31, 2022
teamId = 42 # Arsenal

# EXAMPLE 1: GET LEAGUE
response = requests.request("GET", API_FOOTBALL_ENDPOINT + "/leagues", headers=API_FOOTBALL_HEADERS, 
	params={
		'id': API_FOOTBALL_PREMIER_LEAGUE_ID,
	}
)
with open("out/get_league.json", "w") as outfile:
    outfile.write(json.dumps(json.loads(response.text), indent=4))


# EXAMPLE 2: GET TEAM in LEAGUE in SEASON
response = requests.request("GET", API_FOOTBALL_ENDPOINT + "/teams", headers=API_FOOTBALL_HEADERS, 
	params={
		'league': API_FOOTBALL_PREMIER_LEAGUE_ID, 
		'season': API_FOOTBALL_CURRENT_SEASON,
		'id': teamId
	}
)
with open("out/get_team_in_league_in_season.json", "w") as outfile:
    outfile.write(json.dumps(json.loads(response.text), indent=4))


# EXAMPLE 3: GET PLAYER in LEAGUE in SEASON
response = requests.request("GET", API_FOOTBALL_ENDPOINT + "/players", headers=API_FOOTBALL_HEADERS, 
	params={
		'league': API_FOOTBALL_PREMIER_LEAGUE_ID, 
		'season': API_FOOTBALL_CURRENT_SEASON,
		'team': teamId,
		'id': playerId
	}
)
with open("out/get_player_in_league_in_season.json", "w") as outfile:
    outfile.write(json.dumps(json.loads(response.text), indent=4))
