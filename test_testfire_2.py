import time
from MainPage import LandingPage
from MainPage import LoginPage
from MainPage import UserPage
from Browser import Browser

def test_back (browser):    
    press_sign_in_button = LandingPage()
    press_sign_in_button.button_signin_click()
    time.sleep(2)
    enter_username_and_password = LoginPage()
    enter_username_and_password.enter_login("jsmith")
    time.sleep(2)
    enter_username_and_password.enter_password ("demo1234")
    time.sleep(2)
    enter_username_and_password.click_on_the_button_login()
    time.sleep(2)
    UserPage_is_opened = UserPage()
    UserPage_is_opened.user_page_is_opened()
    press_sign_in_button2 = LandingPage()
    press_sign_in_button2.button_signin_click()
    time.sleep(2)
    back_browser = Browser()
    back_browser.go_back()
    time.sleep(2)
    loginPage_is_opened = LoginPage()
    loginPage_is_opened.login_page_is_opened()
    assert loginPage_is_opened