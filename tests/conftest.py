import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
