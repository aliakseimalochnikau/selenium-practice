'''
- Зайти на сайт https://www.thesaurus.com/
- В поле поиска ввести love
- Нажать иконку поиска
- Найти 6 синоним слова love
- вывести его в консоль
* Для любителей полазить по верстке: вывести на экран все синонимы слова love
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(driver, xpath_value):
    wait = WebDriverWait(driver, 5)
    for condition in [
        EC.presence_of_element_located,
        EC.visibility_of_element_located,
        EC.element_to_be_clickable
    ]:
        wait.until(condition(("xpath", xpath_value)))


class TestLessonTwo:
    def test_find_love_synonyms(self, driver_chrome):
        driver = driver_chrome
        driver.get("https://www.thesaurus.com/")

        # Step 0. Accepting all cookies (Polish reality :/)
        accept_button_xpath = "//*[@id='onetrust-accept-btn-handler']"
        wait(driver, accept_button_xpath)
        accept_button = driver.find_element("xpath", accept_button_xpath)
        accept_button.click()

        # Step 1. Search bar
        search_bar_xpath = "//*[@id='global-search']"
        wait(driver, search_bar_xpath)
        search_bar = driver.find_element("xpath", search_bar_xpath)
        search_bar.send_keys("love")

        # Step 2. Search button
        search_button_xpath = "//*[@class='SFL_CJwX_oOmq1DF63xo']"
        wait(driver, search_button_xpath)
        search_button = driver.find_element("xpath", search_button_xpath)
        search_button.click()

        # Step 3. Synonym button
        synonym_button_xpath = "//*[@data-linkid='y2woe7' and text()='appreciation']"
        wait(driver, synonym_button_xpath)
        synonym_button = driver.find_element("xpath", synonym_button_xpath)
        synonym_button.click()

        # Step 4. Assert and print to console
        word_xpath = "//h1[contains(text(), 'appreciation')]"
        wait(driver, word_xpath)
        word = driver.find_element("xpath", word_xpath)
        expected_result = 'appreciation'
        assert word.text == expected_result, f"Expected '{expected_result}', but got '{word.text}'"
        print(word.text)
