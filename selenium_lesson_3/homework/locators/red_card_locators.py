from selenium.webdriver.common.by import By


class RedCardPageLocators:
    URL = "https://creditcard.alfa-bank.by/RKK?channel=0006"
    PHONE_NUMBER = (By.XPATH, "//*[@type='tel']")
    SUBMIT = (By.XPATH, "//*[@type='submit']")
    TEXT = (By.XPATH, "//*[@class='title' and text()='Пройдите идентификацию']")
    PROCEED_TO_MSI = (By.XPATH, "//*[@type='button']")
