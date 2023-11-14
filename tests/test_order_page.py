import pytest

from data import persons, data
from data.persons import Persons
from data.data import RentalData, TextData
from pages.base_page import BasePage
from pages.order_page import OrderPages


@pytest.mark.fixture('driver')
class TestOrderButton:

    def test_create_order_on_header_button_success(self, driver):
        OrderPages(driver).create_order(persons.name, persons.LASTNAME, persons.ADDRESS, persons.STATION, persons.NUMBER)
        assert TextData.SUCCESSFUL_ORDER_TEXT in persons.new_order_text

    def test_create_order_on_finish_button_success(driver):
        OrderPages(driver).create_order(RentalData.DATA_2)
        assert TextData.SUCCESSFUL_ORDER_TEXT in persons.new_order_text