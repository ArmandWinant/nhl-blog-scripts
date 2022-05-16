import psycopg2
import pandas as pd
import numpy as np
import os
import glob
import re
from datetime import datetime

def parse_record(row_tuples):
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
        
        # parse game information string (date & opoonent)
        m = re.search(r'^\d{4}/\d{2}/\d{2}(vs|@) ([A-Z]){3}$', value)
        if m:
            game_info = parse_game_date(m.group(0))
            if game_info:
                home_game = game_info[0]
                opponent = game_info[1]
                game_date = game_info[2]
                game_season = game_info[3]
                
                data_dict["opponent"] = opponent
                data_dict["home_game"] = home_game
                data_dict["game_date"] = game_date
                data_dict["season"] = f"{game_season}/{game_season+1}"
                continue
        
        if value == "--":
            data_dict[header] = None
            continue
            
        data_dict[header] = value
            
    return data_dict


def parse_game_date(game_string):
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
        
        season_start_year = game_season(date)
        
        return (home_game, opponent, date, season_start_year)
    else:
        return None
    

def game_season(game_date):
    """
    inputs
        game_date (datetime): date of the game
    
    returns:
        season (int): start year of the season
    """
    game_month = game_date.month
    game_year = game_date.year
    
    if game_month < 2 or game_month > 8:
        return game_year
    
    return game_year - 1