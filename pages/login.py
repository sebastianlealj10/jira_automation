from pages.base import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def fill_form(self, username, password):
        email_text_field_elment = self.driver.find_element(*LoginPageLocators.EMAIL_TEXT_INPUT)
        email_text_field_elment.send_keys(username)
        password_text_field_elment = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXT_INPUT)
        password_text_field_elment.send_keys(password)
        email_text_field_elment = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        email_text_field_elment.click()

    def is_error_login(self):
        error_element = None
        try:
            error_element = WebDriverWait(self.driver, 10).\
                until(EC.presence_of_element_located(*LoginPageLocators.ERROR_BLOCK))
        except Exception as e:
            print(f'Element{LoginPageLocators.ERROR_BLOCK} was not found with error e')
        return True if error_element else False
