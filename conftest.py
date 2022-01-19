from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest


@pytest.fixture(autouse=True)
def driver():
    s = Service(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=s)
    driver.get('https://todoist.com/')
    driver.maximize_window()
    yield _driver
    _driver.quit()
