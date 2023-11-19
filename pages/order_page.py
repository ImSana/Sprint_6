import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPages(BasePage):

    def click_cookie_button(self):
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Заполняем поле с именем")
    def set_name_to_field(self, name):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD_LOCATOR, name)

    @allure.step("Заполняем поле с фамилией")
    def set_lastname_to_field(self, lastname):
        self.set_text_to_element(OrderPageLocators.LASTNAME_FIELD_LOCATOR, lastname)

    @allure.step("Заполняем поле с адресом")
    def set_address_to_field(self, address):
        self.set_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step("Заполняем поле с метро")
    def set_station(self, station):
        self.set_text_to_element(OrderPageLocators.STATION_FIELD, station)
        self.driver.find_element(*OrderPageLocators.STATION_DROPDOWN).click()

    @allure.step("Заполняем поле с телефоном")
    def set_number_to_field(self, number):
        self.set_text_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, number)

    @allure.step('Клик по кнопке "Заказать" в шапке')
    def click_order_button_in_header(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Клик по кнопке "Заказать" на странице ')
    def click_order_button_in_footer(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_IN_FOOTER)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    def create_order(self, client):
        self.set_name_to_field(client.get('name'))
        self.set_lastname_to_field(client.get('lastname'))
        self.set_address_to_field(client.get('address'))
        self.set_station(client.get('station'))
        self.set_number_to_field(client.get('number'))

    @allure.step('Заполняем поле "Дата"')
    def set_date(self, date):
        self.set_text_to_element(OrderPageLocators.DATE_FIELD, date)
        self.set_text_to_element(OrderPageLocators.DATE_FIELD, Keys.ENTER)

    def select_rental_period(self, period):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.ONE_DAY)

    @allure.step("Выбираем самокат чёрного цвета")
    def click_checkbox(self, color):
        self.driver.find_element(*color).click()

    @allure.step('Заполняем поле "Комментарий"')
    def set_comment(self, comment):
        self.set_text_to_element(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('Клик по кнопке "Заказ"')
    def click_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Заполнить раздел "Про аренду"')
    def input_rental_information(self, rental_data):
        color_checkbox = {"black": OrderPageLocators.BLACK_CHECKBOX, "grey": OrderPageLocators.GREY_CHECKBOX}
        day_period = {"one": OrderPageLocators.ONE_DAY, "two": OrderPageLocators.TWO_DAY}
        self.set_date(rental_data.get('date'))
        self.select_rental_period(day_period.get(rental_data.get('day')))
        self.click_checkbox(color_checkbox.get(rental_data.get('color')))
        self.set_comment(rental_data.get('comment'))
        self.click_order_button()

    def wait_for_confirm(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(OrderPageLocators.CONFIRM))

    @allure.step('Клик по кнопке "Да" в диалоге подтверждения')
    def click_confirmation_order(self):
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    def wait_for_order_completed(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(OrderPageLocators.ORDER_COMPLETED))

    @allure.step('Получить текст диалога успешного заказа')
    def get_new_order_title(self):
        new_order_text = self.driver.find_element(*OrderPageLocators.ORDER_COMPLETED).text
        return new_order_text

    def wait_for_new_tab(self, number):
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(number))

    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 10).until(ec.url_to_be(url))

