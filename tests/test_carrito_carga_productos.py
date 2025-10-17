from page.carrito_page import Carrito
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time



# test para agregar producto al carrito, validar que se incremente el contador (badge), navegar a la pagina y 
# verificar que se agrego de forma exitosa

def test_carrito1(driver):
    nuevo_carrito = Carrito(driver)
    nuevo_carrito.open()
    nuevo_carrito.login()
    nuevo_carrito.agregarProducto1()
    
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == "1"  

    nuevo_carrito.navegar()
    assert EC.visibility_of_any_elements_located(driver.find_element(By.CLASS_NAME, "cart_contents_container"))

    time.sleep(5)



