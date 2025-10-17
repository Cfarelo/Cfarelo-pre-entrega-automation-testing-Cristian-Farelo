from page.login_Page import Login
import time

def test_login1(driver):
    nuevo_login = Login(driver)
    nuevo_login.open
    nuevo_login.login