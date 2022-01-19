import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestWeb:
    def test_login(self, driver):
        driver.get('http://localhost:8080/secure/Dashboard.jspa')
        driver.maximize_window()
        time.sleep(10)
