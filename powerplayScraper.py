from extract import open_driver, close_driver, wait_for_element
from transforms import parse_record, parse_game_date, game_season
from selenium.webdriver.common.by import By
from scraper import Scraper, get_table_columns, get_table_rows
from sql_queries import summary_table_insert
import urllib.parse
from datetime import datetime
import time


class PowerplayScraper(Scraper):
    def __init__(self):
        super().__init__()