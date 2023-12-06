import pytest


class TestLessonOne:
    @pytest.mark.parametrize("url, page_title", [("https://www.amazon.com/", "Amazon"),
                                                 ("https://www.apple.com/", "Apple"),
                                                 ("https://www.google.com/", "Google")])
    def test_websites_chrome(self, driver_chrome, url, page_title):
        driver_chrome.get(url)
        assert page_title in driver_chrome.title, f"Expected {page_title}, but was {driver_chrome.title}"
        driver_chrome.save_screenshot(f"test_{page_title}.png")
