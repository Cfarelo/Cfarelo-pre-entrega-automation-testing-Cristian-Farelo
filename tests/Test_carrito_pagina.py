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
    driver.save_screenshot("paginaCarrito.png")

    time.sleep(4)