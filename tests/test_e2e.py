import time

from pages.home import HomePage
from pages.login import LoginPage


class TestWeb:
    def test_login(self, driver):
        home_page = HomePage(driver)
        home_page.login()
        login_page = LoginPage(driver)
        login_page.fill_form(username, password)
        assert login_page.is_error_login()
