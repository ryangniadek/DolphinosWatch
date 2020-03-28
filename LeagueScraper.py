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
    return True

def get_level(summoner):
    


# temp execution stuff

dolphinos = cass.get_summoner(name="dolphinos")
print("{name} is a level {level} TURBOVIRGIN on the {region} server".format(name=dolphinos.name, level=dolphinos.level, region=dolphinos.region))