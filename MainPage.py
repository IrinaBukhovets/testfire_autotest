from Browser import Browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, locator):     
        self.locator = locator   

    def unique_find_element(self, browser):
        browser = Browser()   
        browser.find_element(self.locator)  

    def enter_word(self, locator, word):
        Browser().find_element(locator).send_keys(word)

    def click_on_the_button(self, locator, browser):
        browser = Browser()   
        browser.find_element(locator).click()

    def element_is_opened(self, locator, browser):
        browser = Browser()
        browser.find_element(locator).is_displayed()

class LandingPage(BasePage):
     
    locator_sign_in = (By.ID, "LoginLink")

    def __init__(self):
        super().__init__(locator=self.locator_sign_in)

    def button_signin_click(self):
       self.click_on_the_button(locator=self.locator_sign_in, browser = Browser())

    
class LoginPage(BasePage):

    locator_username = (By.CSS_SELECTOR, "#uid")

    licator_password = (By.ID,"passw")

    locator_button_login = (By.XPATH,"//input[@value='Login']")

    def __init__(self):
        super().__init__(locator=self.locator_button_login)

    def enter_login(self, login):
        self.enter_word(locator=self.locator_username, word=login)

    def enter_password(self, password):
        self.enter_word(locator=self.licator_password,word=password)

    def click_on_the_button_login(self):
        self.click_on_the_button(locator=self.locator_button_login, browser=Browser())

    def login_page_is_opened(self):
        self.element_is_opened(locator = self.locator_button_login, browser=Browser())

class UserPage(BasePage):

    locator_button_GO = (By.XPATH,"//input[@value='   GO   ']")

    def __init__(self):
        super().__init__(locator=self.locator_button_GO)

    def user_page_is_opened(self):
        self.element_is_opened(locator = self.locator_button_GO, browser=Browser())