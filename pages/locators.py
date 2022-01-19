from selenium.webdriver.common.by import By


class LoginLocators:
    username_input = (By.ID, 'login-form-username')
    password_input = (By.ID, 'login-form-password')
    logIn_button = (By.ID, 'login-form-submit')


class DashboardLocators:
    dashboard_content = (By.ID, 'dashboard')
