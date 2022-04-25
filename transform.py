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
        
        if value.isalpha():
            # double dashes correspond to missing values
            if value == "--":
                data_dict[header] = np.nan
                continue
            else:
                # leave alphabetical strings unchanged
                data_dict[header] = value
        
        if value.isnumeric():
            # convert all numerical strings to integers
            data_dict[header] = int(value)
            continue
        
        # search for floating number patterns
        m = re.search(r'^\d*\.\d+$', value)
        if m:
            # convert to float value
            data_dict[header] = float(value)
            continue
            
    return data_dict


def parse_game_date(game_string):
    """
    inputs
        game_string (string): no-space string
        
    returns
        two-element tuple: (string, date)
    """
    m1 = re.search(r'[A-Z]+', game_string)
    m2 = re.search(r'\d{4}/\d{2}/\d{2}', game_string)
    
    if m1 and m2:
        oppent = m1.group(0)
        date = m2.group(0)
        
        date = datetime.strptime(date, '%Y/%m/%d')
        
        return (opponent, date)
    else:
        return None
    