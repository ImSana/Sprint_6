import allure
import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from data.data import ListData
from data.urls import DataUrls


@pytest.mark.fixture('driver')
class TestMainPages:
    @pytest.mark.parametrize('index,text', ListData.QUESTIONS_LIST)
    def test_get_answer_on_question(self, driver, index, text):
        page = BasePage(driver)
        page.open_page(DataUrls.SCOOTER_URL)
        questions = MainPage(driver)
        questions.scroll_to_questions()
        questions.click_on_question(index)
        answer = questions.get_answer_text()
        questions.wait_for_get_answer()
        assert answer == text

