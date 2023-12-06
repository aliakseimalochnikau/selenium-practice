from selenium.webdriver.common.by import By


class HomePageLocators:
    URL = "https://myfin.by/"
    CARDS = (By.XPATH, "//*[@href='/cards']")
    RED_CARD = (By.XPATH, "(//*[contains(@data-link, 'RKK')])[1]")
