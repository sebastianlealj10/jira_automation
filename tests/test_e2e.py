import time

from pages.dashboard import DashboardPage
from pages.login import LoginPage


class TestWeb:
    def test_login(self, driver):
        driver.get('http://localhost:8080/login.jsp')
        driver.maximize_window()
        login_page = LoginPage(driver)
        login_page.login_form('sebas', 'sebas10')
        time.sleep(2)
        dashboard_page = DashboardPage(driver)
        assert dashboard_page.is_dashboard_present()
