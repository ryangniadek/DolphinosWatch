# Contains functions to get data from Riot Games API regarding Dolphinos

import pandas as pd
import cassiopeia as cass
import os, sys
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Variables ----------------------------------------------------------------
load_dotenv()
api_key = os.getenv('RIOT_KEY')
cass.set_riot_api_key(api_key)
cass.set_default_region("NA")



# Functions ----------------------------------------------------------------
# Returns true if the specified summoner is currently in a game
def check_if_ingame(summoner):
    result = None
    # Surpress console output. This can be safely removed without
    # breaking functionality, but it made testing a lot easier.
    old_stdout = sys.stdout
    sys.stdout = None
    try:
        match = summoner.current_match
    except:
        result = False
    else:
        result = True
    sys.stdout = old_stdout
    return result

# Gets the cumulative time played (in seconds) for matches that have
# started within the past specified number of hours, up to 7 days
def get_timeplayed(summoner, hrs):
    # Surpress console output. This can be safely removed without
    # breaking functionality, but it made testing a lot easier.
    old_stdout = sys.stdout
    sys.stdout = None
    # Tell user to piss off if they try to query for > 7 days
    if (hrs > (7*24)):
        print("Ya done fucked up, kid")
        return -1
    # Get match history
    hist = summoner.match_history
    now = datetime.now()
    cumulative_time_s = 0
    # Parse through match history
    for match in hist:
        strdate = str(match.creation)
        date = datetime.strptime(strdate.split('T')[0], '%Y-%m-%d')
        # If match occurred within the specified time, add its duration
        # to the cumulative playtime for the past hrs.
        if (now-timedelta(hours=hrs)) <= date <= now:
            t = str(match.duration)
            h, m, s = t.split(':')
            match_time_s = int(h) * 3600 + int(m) * 60 + int(s)
            cumulative_time_s += match_time_s
    sys.stdout = old_stdout
    return cumulative_time_s

# Returns the amount of time, in seconds, a summoner's game lasted
# for a specified game object

# Returns the amount of time, in seconds, a summoner has been in their
# current match, if they are in one.
def get_current_match_time(summoner):
    if (check_if_ingame(summoner)):
        t = str(summoner.current_match.duration)
        h, m, s = t.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        return 0

# Returns a summoner object with the specified name
def get_summoner(summonerName):
    return cass.get_summoner(name=summonerName)
