from pages.base import BasePage
from pages.locators import LoginLocators


class LoginPage(BasePage):
    def login_form(self, user_data):
        username_element = self.driver.find_element(*LoginLocators.username_input)
        username_element.send_keys(user_data[0])
        password_element = self.driver.find_element(*LoginLocators.password_input)
        password_element.send_keys(user_data[1])
        login_button_element = self.driver.find_element(*LoginLocators.logIn_button)
        login_button_element.click()
