from pages.base import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):
    def login(self):
        login_element = self.driver.find_element(*HomePageLocators.LOGIN_LINK)

        login_element.click()

