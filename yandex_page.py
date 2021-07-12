from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from web_page import WebPage
from locator import Locator


class yandex_Locators:

    LOCATOR_SEARCH_INPUT = Locator((By.CLASS_NAME, "input__control"), "Search input /")
    LOCATOR_SEARCH_SUGGEST = Locator((By.CLASS_NAME, "mini-suggest__item"), "suggest /")
    LOCATOR_IMAGES_HREF = Locator((By.CSS_SELECTOR, "[data-id=\"images\"]"), "images href /")


class yandex_page(WebPage):

    def get_input(self):
        return self.find_elements(yandex_Locators.LOCATOR_SEARCH_INPUT)

    def input_send_word(self, word):
        return self.find_element(yandex_Locators.LOCATOR_SEARCH_INPUT).send_keys(word)

    def input_send_ENTER(self):
        return self.find_element(yandex_Locators.LOCATOR_SEARCH_INPUT).send_keys(Keys.ENTER)

    def images_href_click(self):
        return self.find_element(yandex_Locators.LOCATOR_IMAGES_HREF).click()

    def get_suggest(self):
        return self.find_elements(yandex_Locators.LOCATOR_SEARCH_SUGGEST)  