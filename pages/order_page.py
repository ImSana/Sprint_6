import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPages(BasePage):

    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()
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
        self.driver.find_element(*OrderPageLocators.STATION_FIELD).send_keys(station)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(OrderPageLocators.STATION_DROPDOWN))
        self.driver.find_element(*OrderPageLocators.STATION_DROPDOWN).click()
        WebDriverWait(self.driver, 10).until(ec.invisibility_of_element(OrderPageLocators.STATION_DROPDOWN))

    @allure.step("Заполняем поле с телефоном")
    def set_number_to_field(self, number):
        self.set_text_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, number)

    def click_order_button_in_header(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_IN_HEADER)

    def click_to_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    def create_order(self, client):
        self.set_name_to_field(client.get('name'))
        self.set_lastname_to_field(client.get('lastname'))
        self.set_address_to_field(client.get('address'))
        self.set_station(client.get('station'))
        self.set_number_to_field(client.get('number'))
        self.click_to_next_button()

    def wait_for_rent_form(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(OrderPageLocators.RENT_FORM))

    def set_date(self, date):
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(date)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(OrderPageLocators.CALENDAR))
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(ec.invisibility_of_element(OrderPageLocators.CALENDAR))

    def select_rental_period(self, period):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        self.driver.find_element(*period).click()
        WebDriverWait(self.driver, 10).until(ec.invisibility_of_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))

    @allure.step("Выбираем самокат чёрного цвета")
    def set_black_color(self):
        self.click_to_element(OrderPageLocators.BLACK_COLOR_LOCATOR)

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Заполнить раздел "Про аренду"')
    def input_rental_information(self, rental_data):
        color_checkbox = {"black": OrderPageLocators.BLACK_CHECKBOX, "grey": OrderPageLocators.GREY_CHECKBOX}
        day_period = {"one": OrderPageLocators.ONE_DAY, "two": OrderPageLocators.TWO_DAY}
        self.set_date('date')
        self.select_rental_period(day_period.get(rental_data.get('day')))
        self.set_black_color(color_checkbox.get(rental_data.get('color')))
        self.set_comment(rental_data.get('comment'))
        self.click_order_button()

    def wait_for_confirm(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(OrderPageLocators.CONFIRM))

    @allure.step('Клик по кнопке "Да" в диалоге подтверждения')
    def click_confirmation_order(self):
        self.driver.find_element(*OrderPageLocators.YES_BUTTON).click()

    def wait_for_order_completed(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(OrderPageLocators.ORDER_COMPLETED))

    @allure.step('Получить текст диалога успешного заказа')
    def get_new_order_title(self):
        new_order_text = self.driver.find_element(*OrderPageLocators.ORDER_COMPLETED).text
        return new_order_text

    def click_order_status_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_STATUS_BUTTON).click()

    @allure.step('Клик по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*OrderPageLocators.YA_LOGO).click()

    def wait_for_new_tab(self, number):
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(number))

    def wait_for_page_load(self, url):
        WebDriverWait(self.driver, 10).until(ec.url_to_be(url))

    @allure.step('Клик по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*OrderPageLocators.SCOOTER_LOGO).click()

