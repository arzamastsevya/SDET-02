from selenium.webdriver.common.by import By
from web_page import WebPage
from locator import Locator


class yandex_image_Locators:
    
    LOCATOR_IMAGE_CATEGORIES = Locator((By.CLASS_NAME, "PopularRequestList-Item"), "Image category name /image")
 

class yandex_image_page(WebPage):   

    def image_categories_click(self):
        return self.find_element(yandex_image_Locators.LOCATOR_IMAGE_CATEGORIES).click()    

    def get_image_category_name(self):
        return self.find_element(yandex_image_Locators.LOCATOR_IMAGE_CATEGORIES).get_attribute("data-grid-text")