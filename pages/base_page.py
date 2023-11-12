from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

# списал с курса
    def find_my_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(*locator))

# списал с курса
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(*locator))
        self.driver.find_element(*locator).click()

# списал с курса
    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)