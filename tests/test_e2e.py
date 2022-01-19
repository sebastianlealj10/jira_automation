import time

from pages.dashboard import DashboardPage
from pages.login import LoginPage


class TestWeb:
    def test_login(self, driver, user_data):
        login_page = LoginPage(driver)
        login_page.login_form(user_data)
        dashboard_page = DashboardPage(driver)
        assert dashboard_page.is_dashboard_present()
