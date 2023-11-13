import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


# class OrderPage(BasePage):
#
#     @allure.step('Пролистать до кнопки "Заказать" на странице')
#     def scroll_to_order_button(self):
#         button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE)
#         self.driver.execute_script("arguments[0].scrollIntoView();", button)
#         WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(MainPageLocators.ORDER_BUTTON_MAIN_PAGE))
#
#     @allure.step('Клик по кнопке "Заказать" на странице')
#     def click_order_button(self):
#         self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MAIN_PAGE).click()
#
#     @allure.step('Клик по кнопке "Заказать" в шапке')
#     def click_order_button_in_header(self):
#         self.driver.find_element(*MainPageLocators.ORDER_BUTTON_IN_HEADER).click()
#
#     @allure.step('Получить текст заголовка главной страницы')
#     def get_main_header_text(self):
#         return self.driver.find_element(*MainPageLocators.HEADER_TEXT).text
#
class OrderPages(BasePage):

    @allure.step("Заполняем поле с именем")
    def set_name_to_field(self, name_1):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD_LOCATOR, name_1)

    @allure.step("Заполняем поле с фамилией")
    def set_lastname_to_field(self, lastname_1):
        self.set_text_to_element(OrderPageLocators.LASTNAME_FIELD_LOCATOR, lastname_1)

    @allure.step("Заполняем поле с адресом")
    def set_address_to_field(self, address_1):
        self.set_text_to_element(OrderPageLocators.ADDRESS_FIELD, address_1)

    @allure.step("Заполняем поле с метро")
    def set_station_to_field(self, station_1):
        self.set_text_to_element(OrderPageLocators.STATION_FIELD, station_1)

    @allure.step("Заполняем поле с телефоном")
    def set_number_to_field(self, number_1):
        self.set_text_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, number_1)

    def click_to_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Когда привезти")
    def set_number_to_field(self, number_1):
        self.set_text_to_element(OrderPageLocators.ADDRESS_FIELD, number_1)

    # @allure.step("Выбираем самокат чёрного цвета")
    # def set_black_color(self):
    #     self.click_to_element(OrderPageLocators.BLACK_COLOR_LOCATOR)

    # @allure.step("Выбираем самокат серого цвета")
    # def set_grey_color(self):
    #     self.click_to_element(OrderPageLocators.GREY_COLOR_LOCATOR)

    @allure.step("Заказать")
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Проверяем что появилось окно с заказом")
    def check_success_order(self):
        return self.find_my_element(OrderPageLocators.ORDER_COMPLETED)

    def create_order(self, name_1, lastname_1, address_1, station_1):
        self.set_name_to_field(name_1)
        self.set_lastname_to_field(lastname_1)
        self.set_address_to_field(address_1)
        self.set_station_to_field(station_1)
        self.click_to_next_button()
        self.set_black_color()
        self.click_to_order_button()

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

