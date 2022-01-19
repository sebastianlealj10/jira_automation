from pages.base import BasePage
from pages.locators import LoginLocators


class LoginPage(BasePage):
    def login_form(self, username, password):
        username_element = self.driver.find_element(*LoginLocators.username_input)
        username_element.send_keys(username)
        password_element = self.driver.find_element(*LoginLocators.password_input)
        password_element.send_keys(password)
        login_button_element = self.driver.find_element(*LoginLocators.logIn_button)
        login_button_element.click()
