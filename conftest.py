import pytest
from Browser import Browser
from general_config import GeneralConfigs

@pytest.fixture(scope="function")  #Это означает что данная функция-фикстура будет исполнятся только 1 раз за тестовую сессию
def browser():
    browser = Browser()
    browser.set_up_driver()
    browser.go_to_site(GeneralConfigs.BASE_URL)
    yield browser
    browser.quit()
