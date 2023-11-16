import allure
import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from data.urls import DataUrls
from data.data import TextData
from pages.order_page import OrderPages


@pytest.mark.usefixtures("driver")
class TestLogo:
    @allure.title('Открытие сайта Самоката по логотипу "Самокат"')
    @allure.description('На странице заказа нажать на логотип "Самокат", выполнен переход на главную страницу Самоката')
    def test_main_page_open_by_scooter_logo(self, driver):
        order_pages = BasePage(driver)
        order_pages.open_page(DataUrls.ORDER_SCOOTER_URL)
        pages = MainPage(driver)
        pages.click_scooter_logo()
        order_pages.wait_for_page_load(DataUrls.SCOOTER_URL)
        current_header_text = MainPage(driver).get_main_header_text()
        header_text = TextData.HEADER_TEXT
        assert driver.current_url == DataUrls.SCOOTER_URL and header_text == current_header_text

    @allure.title('Открытие сайта Дзен по логотипу "Яндекс"')
    @allure.description('На странице заказа нажать на логотип "Яндекс", выполнен переход на страницу Дзен')
    def test_dzen_page_open_by_yandex_logo(self, driver):
        order_pages = BasePage(driver)
        order_pages.open_page(DataUrls.ORDER_SCOOTER_URL)
        pages = MainPage(driver)
        pages.click_yandex_logo()
        assert driver.current_url != DataUrls.DZEN_URL