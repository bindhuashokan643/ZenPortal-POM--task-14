import password
import self

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.logger import LogGenerator
from utilities.read_json import ReadJson


class TestLogin:

    log = LogGenerator.loggen()
    data = ReadJson.get_config()

    def test_successful_login(self,setup):
        self.driver = setup
        lp = LoginPage(self.driver)
        assert "dashboard" in self.driver.current_url
        lp.login(
            self.data["Valid_user"]["email"],
            self.data["Valid_user"]["password"]
        )
        self.log.info("Login successful")
        assert "dashboard" in self.driver.current_url

    def test_unsuccessful_login(self,setup):
        self.driver = setup
        lp = LoginPage(self.driver)
        lp.login(
            self.data["Invalid_user"]["email"],
            self.data["Invalid_user"]["password"]
        )
        assert "Invalid" in lp.error_message()

    def test_username_textbox(self,setup):
        self.driver = setup
        lp = LoginPage(self.driver)
        assert lp.is_username_displayed()

    def text_password_textbox(self,setup):
        self.driver = setup
        lp = LoginPage(self.driver)
        assert lp.is_password_displayed()

    def test_logout(self,setup):
        self.driver = setup
        lp = LoginPage(self.driver)
        lp.login(
            self.data["Valid_user"]["email"],
            self.data["Valid_user"]["password"]
        )
        dashboard = DashboardPage(self.driver)
        dashboard.logout()
        assert "login" in self.driver.current_url