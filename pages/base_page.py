from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def click(self, locator):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            element.click()

        except TimeoutException:
            raise Exception(f"Element not clickable {locator}")

    def enter_text(self,locator, value):
        try:
            element = self.wait.until(
              EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(value)

        except NoSuchElementException:
            raise Exception(f"Element not found  {locator}")

    def get_element(self,locator):

         return self.wait.until(
             EC.visibility_of_element_located(locator)
         )

