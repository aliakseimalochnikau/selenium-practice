from selenium_lesson_3.homework.locators.home_locators import HomePageLocators
from selenium_lesson_3.homework.pages.base_page import BasePage


class HomePage(BasePage):

    def home_page_is_expected(self) -> None:
        assert HomePageLocators.URL in self.get_current_url()

    def navigate_to_cards(self) -> None:
        self.move_to_element(HomePageLocators.CARDS)

    def proceed_to_red_card(self) -> None:
        self.click(HomePageLocators.RED_CARD)
