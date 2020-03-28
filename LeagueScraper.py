# Contains functions to get data from Riot Games API regarding Dolphinos

import pandas as pd
import cassiopeia as cass
import os
from dotenv import load_dotenv

# variables n shit
load_dotenv()
api_key = os.getenv('RIOT_KEY')
cass.set_riot_api_key(api_key)
cass.set_default_region("NA")



# functions ----------------------------------------------------------------
# Returns a boolean value if dolphinos is currently in a game
def check_if_ingame(summoner):
    try:
        match = summoner.current_match
    except:
        return False
    else:
        return True

# Returns the amount of time, in seconds, a summoner has been in a match
def get_match_time(summoner):
    return 0

# Returns the level of the specified summoner
def get_level(summoner):
    return 0

# Returns a summoner object with the specified name
def get_summoner(summonerName):
    return cass.get_summoner(name=summonerName)

# testing

nightblue = get_summoner("Nightblue3")
dolphinos = get_summoner("dolphinos")

print("Nightblue3 in game? " + str(check_if_ingame(nightblue)))
print("dolphinos in game? " + str(check_if_ingame(dolphinos)))