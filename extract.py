from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def open_driver():
    """
    returns
        driver (webdriver.Chrome): instance of Chrome WebDriver
    """
    driver_executable = "/Users/bastienwinant/Desktop/SeleniumDrivers/chromedriver"
    
    chrome_service = Service(driver_executable)
    
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    
    driver = webdriver.Chrome(service=chrome_service, options=options)
    
    return driver



def close_driver(driver):
    driver.close()
    
    
def wait_for_element(source, search_by, target, timeout=20, unique_element=False):
    """
    inputs:
        source ():
    """
    try:
        if unique_element:
            elements = WebDriverWait(source, timeout=timeout).until(lambda d: d.find_element(search_by, target))
        else:
            elements = WebDriverWait(source, timeout=timeout).until(lambda d: d.find_elements(search_by, target))
        
    except TimeoutException:
        elements = []
    
    return elements