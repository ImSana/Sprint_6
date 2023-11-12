from data.data import RentalData
from pages.base_page import BasePage
from pages.order_page import OrderPages


class TestOrderButton(BasePage):

    def test_create_order_on_header_button_success(driver):
        OrderPages(driver).create_order(RentalData.DATA_1)
        assert OrderPages(driver).check_success_order()

    def test_create_order_on_finish_button_success(driver):
        OrderPages(driver).create_order(RentalData.DATA_2)
        assert OrderPages(driver).check_success_order()