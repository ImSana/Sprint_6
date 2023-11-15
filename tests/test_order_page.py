import pytest
from data.data import RentalData, TextData, Clients
from data.urls import DataUrls
from pages.base_page import BasePage
from pages.order_page import OrderPages


@pytest.mark.fixture('driver')
class TestOrderButton:

    def test_order_button_on_header(self, driver):
        page = BasePage(driver)
        page.open_page(DataUrls.SCOOTER_URL)
        order_pages = OrderPages(driver)
        order_pages.click_cookie_button()
        order_pages.click_order_button_in_header()
        order_pages.create_order(Clients.CLIENT_1)
        order_pages.click_next_button()
        order_pages.wait_for_rent_form()
        order_pages.input_rental_information(RentalData.DATA_1)
        order_pages.wait_for_confirm()
        order_pages.click_confirmation_order()
        order_title = order_pages.get_new_order_title()
        order_pages.wait_for_order_completed()
        assert TextData.SUCCESSFUL_ORDER_TEXT in order_title
