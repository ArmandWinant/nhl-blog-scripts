from extract import open_driver, close_driver, wait_for_element
from DML import db_connect, close_db_connect
from selenium.webdriver.common.by import By
from psycopg2.extras import execute_batch


def get_table_columns(table_element):
    header_container = wait_for_element(source=table_element, search_by=By.CLASS_NAME, target="table-header-container", unique_element=True)
    header_elements = wait_for_element(source=header_container, search_by=By.CLASS_NAME, target="rt-th")
    header_names = [header.text for header in header_elements]
    
    return header_names


def get_table_rows(table_element):
    table_rows = wait_for_element(source=table_element, search_by=By.CLASS_NAME, target="rt-tbody", unique_element=True)
    rows = wait_for_element(source=table_rows, search_by=By.CLASS_NAME, target="rt-tr")
    
    return rows


class Scraper:
    def __init__(self):
        self.driver = None
        self.conn = None
        self.cur = None
        
        self.table_data = None
        self.table_headers = None
        self.table_insert = ""
        self.staged_data = []
        
        self.base_url = "https://www.nhl.com/stats/teams?"
        self.url_dict = {
            "aggregate": 0,
            "reportType": "game",
            "pageSize": 100
        }
    
    
    # SELENIUM DRIVER
    def open_driver(self):
        self.driver = open_driver()
    
    def close_driver(self):
        if self.driver:
            close_driver(self.driver)
            
    # POSTGRESQL DATABASE
    def db_connect(self):
        self.conn, self.cur = db_connect()
    
    def close_db_connect(self):
        if self.conn and self.cur:
            close_db_connect(self.conn, self.cur)
    
    
    def build_url(self, playoffs, start, end=None):
        if playoffs:
            self.url_dict["gameType"] = 3
        else:
            self.url_dict["gameType"] = 2
        
        if (isinstance(start, str) and start.isnumeric()) or isinstance(start, int):
            start = int(start)
            self.url_dict["seasonFrom"] = f"{start}{start+1}"
            self.url_dict["seasonTo"] = f"{start}{start+1}"
            
            self.url_dict["dateFromSeason"] = []
                
    
    def load(self):
        execute_batch(self.cur, self.table_insert, self.staged_data)
        print(f"Loaded {len(self.staged_data)} records")
        
        