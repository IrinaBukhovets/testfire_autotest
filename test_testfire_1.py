import time
from MainPage import LandingPage
from MainPage import LoginPage
from MainPage import UserPage
from config import LOGIN
from config import PASSWORD

def test_login (browser):    

    press_sign_in_button = LandingPage()
    press_sign_in_button.button_signin_click()
    time.sleep(2)
    enter_username_and_password = LoginPage()
    enter_username_and_password.enter_login(LOGIN)
    time.sleep(2)
    enter_username_and_password.enter_password(PASSWORD)
    time.sleep(2)
    enter_username_and_password.click_on_the_button_login()
    time.sleep(2)
    UserPage_is_opened = UserPage()
    UserPage_is_opened.user_page_is_opened()
    assert UserPage_is_opened

