from selenium_lesson_3.homework.locators.home_locators import HomePageLocators
from selenium_lesson_3.homework.locators.red_card_locators import RedCardPageLocators
from selenium_lesson_3.homework.pages.home_page import HomePage
from selenium_lesson_3.homework.pages.red_card_page import RedCardPage
from selenium_lesson_3.homework.utils.color_utils import ColorUtils


class TestRedCard:
    def test_applying_for_red_card(self, driver):
        home_page = HomePage(driver, HomePageLocators.URL)
        home_page.open_page()
        home_page.home_page_is_expected()
        home_page.navigate_to_cards()
        home_page.proceed_to_red_card()
        driver.switch_to.window(driver.window_handles[-1])
        red_card_page = RedCardPage(driver, RedCardPageLocators)
        red_card_page.red_card_page_is_expected()
        red_card_page.input_phone_number()
        red_card_page.submit_phone_number()

        # Assert text is present
        text_element = red_card_page.assert_element(RedCardPageLocators.TEXT)

        # Assert text is the expected one
        expected_text = "Пройдите идентификацию"
        assert expected_text in text_element.text, f"Wrong text: Expected {expected_text}, but got {text_element.text}"

        # Assert "Proceed to MSI" is present
        button = red_card_page.assert_element(RedCardPageLocators.PROCEED_TO_MSI)

        # Assert "Proceed to MSI" button name is the expected one
        expected_button_name = "Перейти в МСИ"
        assert expected_button_name in button.text, (f"Wrong button name: Expected {expected_button_name},"
                                                     f" but got {button.text}")

        # Assert "Proceed to MSI" button color
        color = ColorUtils.rgba_to_hex(button.value_of_css_property("background-color"))
        expected_color = "#ef3124"
        assert color == expected_color, f"Wrong color: Expected '{expected_color}, but got '{color}'"



