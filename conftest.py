import pytest
from selenium import webdriver


@pytest.fixture
def driver_chrome():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(chrome_options)
    return driver
