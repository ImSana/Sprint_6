import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, expected_conditions
from locators.base_page_locators import BasePageLocators


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

    @allure.step('Клик по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YA_LOGO).click()

    def wait_for_new_tab(self, number):
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(number))

    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 10).until(ec.url_to_be(url))

    @allure.step('Клик по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.SCOOTER_LOGO).click()

    @allure.step('Открыть страницу {page}')
    def open_page(self, page):
        self.driver.get(page)
