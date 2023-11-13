import pytest

from data import persons
from data.persons import Persons
from data.data import RentalData
from pages.base_page import BasePage
from pages.order_page import OrderPages


@pytest.mark.fixture('driver')
class TestOrderButton:

    def test_create_order_on_header_button_success(driver):
        OrderPages(driver).create_order (persons.Persons.name_1, persons.Persons.lastname_1, persons.Persons.address_1)
        assert OrderPages(driver).check_success_order()

    def test_create_order_on_finish_button_success(driver):
        OrderPages(driver).create_order(RentalData.DATA_2)
        assert OrderPages(driver).check_success_order()