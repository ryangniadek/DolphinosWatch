# Contains functions to get data from Riot Games API regarding Dolphinos

from riotwatcher import LolWatcher, ApiError
import pandas as pd


# variables n shit
server = "na1.api.riotgames.com/"
all_data = "liveclientdata/allgamedata"
api_key = 'RGAPI-229b6327-d063-4a8b-9da7-1d873f7dd99f'
watcher = LolWatcher(api_key)
my_region = 'na1'

dolphinos = watcher.summoner.by_name(my_region, 'dolphinos')

# functions ----------------------------------------------------------------
# Returns a boolean value if dolphinos is currently in a game
def check_if_ingame():
    return True

# Returns the latest match
def latest_match():
    matches = watcher.match.matchlist_by_account(my_region, dolphinos['accountId'])
    return matches['matches'][0]


# temp execution stuff
print(latest_match())