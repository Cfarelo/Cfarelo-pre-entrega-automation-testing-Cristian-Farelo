from page.login_Page import Login
from selenium.webdriver.common.by import By
import time

#test del catalogo de productos y el componente "filtros"

def test_catalogo1(driver):
    nuevo_login = Login(driver)
    nuevo_login.open()
    nuevo_login.login()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    filtros = driver.find_elements(By.CSS_SELECTOR, "div.right_component .select_container")
    assert len(filtros) > 0
    
    

    time.sleep(5)