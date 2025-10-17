from page.login_Page import Login
from selenium.webdriver.common.by import By
import time

def test_login1(driver):
    nuevo_login = Login(driver)
    nuevo_login.open()
    nuevo_login.login()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    #titulo = driver.find_element(By.CLASS_NAME, "app_logo")
    #assert titulo == "Swag Labs"

    time.sleep(5)