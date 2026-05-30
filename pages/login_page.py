from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.ID, "loginButton")
    error_message = (By.XPATH, "//div[contains(text(),'Invalid')]")

    def __init__(self,driver):
        super().__init__(driver)

    def login(self,username,password):
        self.enter_text(self.username,username)
        self.enter_text(self.password,password)
        self.click(self.login_button)

    def is_username_displayed(self):
        return self.get_element(self.username).is_displayed()

    def is_password_displayed(self):
        return self.get_element(self.password).is_displayed()

    def get_error_message(self):
        return self.get_element(self.error_message).text