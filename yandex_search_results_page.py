from selenium.webdriver.common.by import By
from web_page import WebPage
from locator import Locator


class yandex_search_Locators:

    LOCATOR_HREF = Locator((By.CLASS_NAME, "OrganicTitle-Link"), "search result href /search")
    

class yandex_search_results_page(WebPage):

    def get_href_URLs(self):
        href_URL_list = []
        elements=self.find_elements(yandex_search_Locators.LOCATOR_HREF)
        for element in elements:
            href_URL_list.append(element.get_attribute("href"))          
        return href_URL_list
