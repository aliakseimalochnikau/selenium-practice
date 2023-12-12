from selenium_lesson_3.homework.config.data import Data
from selenium_lesson_3.homework.locators.red_card_locators import RedCardPageLocators
from selenium_lesson_3.homework.pages.base_page import BasePage


class RedCardPage(BasePage):
    def red_card_page_is_expected(self) -> None:
        assert RedCardPageLocators.URL in self.get_current_url()

    def input_phone_number(self) -> None:
        self.send_text(RedCardPageLocators.PHONE_NUMBER, Data.PHONE_NUMBER)

    def submit_phone_number(self) -> None:
        self.click(RedCardPageLocators.SUBMIT)
