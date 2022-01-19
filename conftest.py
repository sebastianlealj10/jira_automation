import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest


@pytest.fixture(autouse=True)
def driver():
    s = Service(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=s)
    _driver.get(f'{os.environ["env"]}login.jsp')
    _driver.maximize_window()
    yield _driver
    _driver.quit()


@pytest.fixture(autouse=True)
def user_data():
    user_data = (os.environ["username"], os.environ["password"])
    return user_data
