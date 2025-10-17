from page.carrito_page import Carrito
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# test para remover productos del carrito y revisar que quede vacio

def test_carrito2(driver):
    nuevo_carrito2 = Carrito(driver)
    nuevo_carrito2.open()
    nuevo_carrito2.login()
    nuevo_carrito2.agregarProducto1()
    nuevo_carrito2.navegar()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"
    time.sleep(3)
    nuevo_carrito2.borrarProducto()
    assert EC.invisibility_of_element(driver.find_element(By.CLASS_NAME, "cart_contents_container"))


    time.sleep(4)