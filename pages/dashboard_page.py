from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    loggout_btn = (By.XPATH, "//button[contains(text(),'Logout')]")

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.click(self.loggout_btn)