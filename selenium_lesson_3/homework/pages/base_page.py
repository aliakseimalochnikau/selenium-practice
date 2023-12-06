from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=1)

    def assert_element(self, locator: tuple, clickable=False, return_many=False) -> WebElement:
        self.wait.until(EC.presence_of_element_located(locator))
        self.wait.until(EC.visibility_of_element_located(locator))
        if clickable:
            self.wait.until(EC.element_to_be_clickable(locator))

        if return_many:
            result = self.driver.find_elements(*locator)
        else:
            result = self.driver.find_element(*locator)
        return result

    def click(self, locator: tuple) -> None:
        element = self.assert_element(locator, clickable=True)
        element.click()

    def open_page(self) -> None:
        self.driver.get(self.url)

    # def is_page_opened(self):
    #     self.wait.until(EC.url_contains(self.url))

    def get_current_url(self) -> str:
        return self.driver.current_url

    def send_text(self, locator: tuple, value: str) -> None:
        element = self.assert_element(locator, clickable=True)
        element.send_keys(value)

    def move_to_element(self, locator: tuple) -> None:
        element = self.assert_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
