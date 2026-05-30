from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)
            return driver
        raise Exception("Browser not supported")

    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
        }
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)
        return driver