# import psycopg2
import pandas as pd
# import numpy as np
import os
import glob
import re
from datetime import datetime

def parse_record(row_tuples, playoffs=False):
    """
    inputs
        row_tuples (lst): list of string tuples, (header, value)
    
    return
        data_dict (dict): parsed key-value pairs
    """
    data_dict = {}
    
    for t in row_tuples:
        header, value = t # unpack tuple values
        
        # remove any leading/trailing spaces
        value = value.strip()
        header = header.strip()
           
        # all alphabetical strings are returned unchanged
        if value.isalpha():
            data_dict[header] = value
            continue
        
        m = re.search(r'^-*\d+$', value)
        if value.isnumeric() or m:
            # convert all numerical strings to integers
            data_dict[header] = int(value)
            continue
        
        # search for floating number patterns
        m = re.search(r'^-*\d*\.\d+$', value)
        if m:
            # convert to float value
            data_dict[header] = float(value)
            continue
        
        # search for mm:ss format string
        m = re.search(r'^\d{1,2}:\d{2}$', value)
        if m:
            seconds_int = time_str_to_int(m.group(0))
            data_dict[header] = seconds_int
            continue
        
        # parse game information string (date & opponent)
        m = re.search(r'^\d{4}/\d{2}/\d{2}(vs|@) ([A-Z]){3}$', value)
        if m:
            game_info = parse_game_date(m.group(0), playoffs=playoffs)
            if game_info:
                home_game = game_info[0]
                opponent = game_info[1]
                game_date = game_info[2]
                game_season = game_info[3]
                
                data_dict["opponent"] = opponent
                data_dict["home_game"] = home_game
                data_dict["game_date"] = game_date
                data_dict["season"] = f"{game_season}/{str((game_season+1)%100).zfill(2)}"
                continue
        
        if value == "--":
            data_dict[header] = None
            continue
            
        data_dict[header] = value
            
    return data_dict


def parse_game_date(game_string, playoffs=False):
    """
    inputs
        game_string (string): no-space string
        
    returns
        two-element tuple: (string, date)
    """
    home_game = True if "vs" in game_string else False
    
    m1 = re.search(r'[A-Z]{3}$', game_string)
    m2 = re.search(r'^\d{4}/\d{2}/\d{2}', game_string)
    
    if m1 and m2:
        opponent = m1.group(0)
        date = m2.group(0)
        
        # convert date string to datetime object
        date = datetime.strptime(date, '%Y/%m/%d').date()
        
        season_start_year = game_season(date, playoffs=playoffs)

        return (home_game, opponent, date, season_start_year)
    else:
        return None
    

def game_season(game_date, playoffs):
    """
    inputs
        game_date (datetime): date of the game
    
    returns:
        season (int): start year of the season
    """
    game_month = game_date.month
    game_year = game_date.year
    
    if playoffs:
        return game_year - 1
    
    if game_month > 8:
        return game_year
    
    return game_year - 1


def time_str_to_int(time_string):
    """
    converts time given as a string (mm:ss) to an integer representing seconds 
    """
    time_list = time_string.split(":")
    
    minutes = int(time_list[0].strip())
    seconds = int(time_list[1].strip())
    
    time_int = minutes * 60 + seconds
    
    return time_int