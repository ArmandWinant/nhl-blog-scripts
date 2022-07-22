from extract import open_driver, close_driver, wait_for_element
from transforms import parse_record, parse_game_date, game_season
from selenium.webdriver.common.by import By
from scraper import Scraper, get_table_columns, get_table_rows
from sql_queries import summary_table_insert
import urllib.parse
from datetime import datetime
import time


class SummaryScraper(Scraper):
    def __init__(self):
        super().__init__()
        self.table_insert = summary_table_insert      
    
    
    def transform(self, headers, row_elements):
        playoffs = self.url_dict["gameType"] == 3
        
        for row in row_elements:
            row_cells = wait_for_element(source=row, search_by=By.CLASS_NAME, target="rt-td")
            row_values = [cell.text for cell in row_cells]
            
            values_map = list(zip(headers, row_values))
            map_dict = parse_record(values_map, playoffs=playoffs)

            self.cur.execute("SELECT abbreviation FROM teams WHERE team = %s;", (map_dict["Team"],))
            team_abbreviation = self.cur.fetchone()[0]
            
            if playoffs:
                ordered_data_list = [
                    team_abbreviation,
                    map_dict["season"],
                    map_dict["game_date"],
                    map_dict["home_game"],
                    map_dict["opponent"],
                    map_dict["W"],
                    map_dict["L"],
                    map_dict["T"],
                    None,
                    map_dict["P"],
                    map_dict["P%"],
                    map_dict["RW"],
                    map_dict["ROW"],
                    map_dict["S/O Win"],
                    map_dict["GF"],
                    map_dict["GA"],
                    map_dict["PP%"],
                    map_dict["PK%"],
                    map_dict["Net PP%"],
                    map_dict["Net PK%"],
                    map_dict["Shots/GP"],
                    map_dict["GA/GP"],
                    map_dict["FOW%"],
                    playoffs
                ]
            else:
                ordered_data_list = [
                    team_abbreviation,
                    map_dict["season"],
                    map_dict["game_date"],
                    map_dict["home_game"],
                    map_dict["opponent"],
                    map_dict["W"],
                    map_dict["L"],
                    map_dict["T"],
                    map_dict["OT"],
                    map_dict["P"],
                    map_dict["P%"],
                    map_dict["RW"],
                    map_dict["ROW"],
                    map_dict["S/O Win"],
                    map_dict["GF"],
                    map_dict["GA"],
                    map_dict["PP%"],
                    map_dict["PK%"],
                    map_dict["Net PP%"],
                    map_dict["Net PK%"],
                    map_dict["Shots/GP"],
                    map_dict["GA/GP"],
                    map_dict["FOW%"],
                    playoffs
                ]
                    
            self.staged_data.append(ordered_data_list)
            
            
    def extract(self, url):
        """sends requests to the url and scrapes the table elements (header and rows)"""
        self.url_dict["page"] = 0
        self.staged_data = []
        errors = 0
        
        while True:
            url = self.base_url + urllib.parse.urlencode(self.url_dict)

            self.driver.get(url)
            try:
                # scrape the page's main table
                root_element = wait_for_element(source=self.driver, search_by=By.ID, target="root", unique_element=True)

                pagination = wait_for_element(source=root_element, search_by=By.CLASS_NAME, target="pagination", unique_element=True)
                page_number_field = wait_for_element(source=pagination, search_by=By.TAG_NAME, target="input", unique_element=True)
                total_pages = int(page_number_field.get_attribute('max'))

                data_table = wait_for_element(source=root_element, search_by=By.CLASS_NAME, target="rt-table", unique_element=True)

                table_headers = get_table_columns(data_table)
                row_elements = get_table_rows(data_table)

                self.transform(table_headers, row_elements)

                self.url_dict["page"] += 1

                errors = 0

            except AttributeError:
                errors += 1

                if errors == 3:
                    self.url_dict["page"] += 1
                    print("Skipped page ", self.url_dict["page"])
            
            if self.url_dict["page"] >= total_pages:
                break
                    
                    
    def etl(self, start, playoffs=False):
        # the chrome driver and database cursor are used in multiple scripts
        self.open_driver()
        self.db_connect()
        
        self.build_url(start=start, playoffs=playoffs)
        self.extract(start)
        self.load()
        
        # close the driver and the cursor
        self.close_driver()
        self.close_db_connect()