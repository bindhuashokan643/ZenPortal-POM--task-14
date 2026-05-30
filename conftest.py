import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.wpewebkit import options


@pytest.fixture
def setup():
    chrome_options = Options()
    prefs = {"profile.default_content_settings_values.notifications": 2,}
    options.add_expermental_option("prefs", prefs)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://v2.zenclass.in/login")
    yield driver
    driver.quit()