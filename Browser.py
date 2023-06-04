from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Singletone import Singletone

class Browser(metaclass=Singletone):
    def __init__(self):
        self.webdriver = {}

    def set_up_driver(self):
        #self.webdriver["edge"] = webdriver.Edge(executable_path="C:\\Users\\User\\Desktop\\msedgedriver.exe")
        self.webdriver["edge"] = webdriver.Firefox()
        
    def get_driver(self):
        return self.webdriver["edge"]
    
    def find_element(self,locator,time=5):   
        return WebDriverWait(self.get_driver(),time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
    
    def go_back(self):
        self.get_driver().back()

    def refresh(self):
        self.get_driver().refresh()

    def go_to_site(self, url):
        self.get_driver().get(url)

    def quit(self):
        self.get_driver().quit()
        self.webdriver.pop("edge", None)
