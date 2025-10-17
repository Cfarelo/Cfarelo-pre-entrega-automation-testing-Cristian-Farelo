from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time



URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def get_driver():
    #driver = webdriver.Chrome()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    

    time.sleep(5)
    return driver