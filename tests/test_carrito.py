from page.carrito_page import Carrito
from selenium.webdriver.common.by import By
import time


#navegar a la pagina del carrito para visualizarlo
def test_carrito2(driver):
    nuevo_carrito = Carrito(driver)
    nuevo_carrito.open()
    nuevo_carrito.login()
    nuevo_carrito.navegar()
    assert "/cart.html" in driver.current_url


    time.sleep(4)

#agregar producto al carrito
def test_carrito1(driver):
    nuevo_carrito = Carrito(driver)
    nuevo_carrito.open()
    nuevo_carrito.login()
    
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    
    assert len(products) > 0

    products[0].find_element(By.TAG_NAME, 'button').click()

    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == "1"  
       
    time.sleep(5)



