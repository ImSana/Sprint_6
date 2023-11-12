import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()

    @allure.step('Пролистать до раздела "Вопросы о важном"')
    def scroll_to_questions(self):
        faq = self.driver.find_element(*MainPageLocators.FAQ)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(MainPageLocators.FAQ))

    def get_questions(self):
        return self.driver.find_elements(*MainPageLocators.QUESTIONS)

