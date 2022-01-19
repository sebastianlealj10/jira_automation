from pages.base import BasePage
from pages.locators import DashboardLocators

from wrappers.element_exists import is_element_present


class DashboardPage(BasePage):
    def is_dashboard_present(self):
        return is_element_present(self.driver, *DashboardLocators.dashboard_content)
