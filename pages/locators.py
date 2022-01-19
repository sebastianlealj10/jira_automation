from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/users/showlogin"]')


class LoginPageLocators:
    EMAIL_TEXT_INPUT = (By.ID, 'email')
    PASSWORD_TEXT_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button')
    ERROR_BLOCK = (By.CLASS_NAME, 'error_block')
