from page.login_Page import Login
from selenium.webdriver.common.by import By
import time

def test_login1(driver):
    nuevo_login = Login(driver)
    nuevo_login.open()
    nuevo_login.login()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_label .app_logo').text
    assert titulo == 'Swag Labs'
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'
    

    time.sleep(5)