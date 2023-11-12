import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


@allure.step('Пролистать до кнопки "Заказать" на странице')
def scroll_to_order_button(self):
    button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE)
    self.driver.execute_script("arguments[0].scrollIntoView();", button)
    WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(MainPageLocators.ORDER_BUTTON_MAIN_PAGE))


@allure.step('Клик по кнопке "Заказать" на странице')
def click_order_button(self):
    self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE).click()


@allure.step('Клик по кнопке "Заказать" в шапке')
def click_order_button_in_header(self):
    self.driver.find_element(*MainPageLocators.ORDER_BUTTON_IN_HEADER).click()


@allure.step('Получить текст заголовка главной страницы')
def get_main_header_text(self):
    return self.driver.find_element(*MainPageLocators.HEADER_TEXT).text


class OrderPages(BasePage):

    @allure.step("Заполняем поле с именем")
    def set_name_to_field(self, name):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD_LOCATOR, name)

    @allure.step("Заполняем поле с фамилией")
    def set_lastname_to_field(self, lastname):
        self.set_text_to_element(OrderPageLocators.LASTNAME_FIELD_LOCATOR, lastname)

    @allure.step("Выбираем самокат чёрного цвета")
    def set_black_color(self):
        self.click_to_element(OrderPageLocators.BLACK_COLOR_LOCATOR)

    @allure.step("Выбираем самокат чёрного цвета")
    def set_grey_color(self):
        self.click_to_element(OrderPageLocators.GREY_COLOR_LOCATOR)

    @allure.step("Заказать")
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Проверяем что появилось окно с заказом")
    def check_success_order(self):
        return self.find_my_element(OrderPageLocators.ORDER_COMPLETED)

    def create_order(self, name, lastname):
        self.set_name_to_field(name)
        self.set_lastname_to_field(lastname)
        self.set_black_color()
        self.click_to_order_button()



