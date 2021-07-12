from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from web_page import WebPage
from locator import Locator
import hashlib


class yandex_image_search_Locators:
    

    LOCATOR_SEARCH_INPUT = Locator((By.CLASS_NAME, "input__control"), "Search input /images/search")
    LOCATOR_ACTIVE_TAB = Locator((By.CLASS_NAME, "tabs-navigation__tab_selected_yes"), "Active tab /images/search")
    LOCATOR_IMAGE_RESULT = Locator((By.CLASS_NAME, "serp-item__preview"), "Search result preview /images/search")

    LOCATOR_IMAGE_OPENED = Locator((By.CLASS_NAME, "MediaViewer-View"), "Image opened /images/search")
    LOCATOR_IMAGE_ORIGIN = Locator((By.CLASS_NAME, "MMImage-Origin"), "Image origin /images/search")

    LOCATOR_IMAGE_NEXT_BTN = Locator((By.CLASS_NAME, "CircleButton_type_next"), "Image next button /images/search")
    LOCATOR_IMAGE_PREVIOUS_BTN = Locator((By.CLASS_NAME, "CircleButton_type_prev"), "Image previous button /images/search")


class yandex_image_search_page(WebPage):   


    def get_main_input_text(self):
        return self.find_element(yandex_image_search_Locators.LOCATOR_SEARCH_INPUT).get_attribute('value')

    def get_active_tab(self):
        return self.find_element(yandex_image_search_Locators.LOCATOR_ACTIVE_TAB).text

    def image_1st_results_click(self):
        return self.find_element(yandex_image_search_Locators.LOCATOR_IMAGE_RESULT).click()

    def image_opened(self):
        return self.find_element(yandex_image_search_Locators.LOCATOR_IMAGE_OPENED)

    def image_opened_focus(self):
        return ActionChains(self.driver).move_to_element(self.find_element(yandex_image_search_Locators.LOCATOR_IMAGE_OPENED)).perform()     

    def get_image_next_btn(self):
        self.image_opened_focus()
        return self.find_element(yandex_image_search_Locators.LOCATOR_IMAGE_NEXT_BTN)

    def get_image_previous_btn(self):
        self.image_opened_focus()
        return self.find_element(yandex_image_search_Locators.LOCATOR_IMAGE_PREVIOUS_BTN)

    def image_next_btn_focus(self):
        return ActionChains(self.driver).move_to_element(self.find_element(yandex_image_search_Locators.LOCATOR_IMAGE_NEXT_BTN)).perform() 

    def image_next_click(self):
        self.image_opened_focus()
        return self.find_element(yandex_image_search_Locators.LOCATOR_IMAGE_NEXT_BTN).click()

    def image_previous_click(self):
        self.image_opened_focus()
        return self.find_element(yandex_image_search_Locators.LOCATOR_IMAGE_PREVIOUS_BTN).click()

    def get_md5_image_screenshot(self): 
        self.image_next_btn_focus()
        return hashlib.md5(self.find_element(yandex_image_search_Locators.LOCATOR_IMAGE_OPENED).screenshot_as_png).hexdigest()

    def get_image_origin_url(self):
        self.get_image_next_btn()
        self.get_image_previous_btn()
        return self.find_elements(yandex_image_search_Locators.LOCATOR_IMAGE_ORIGIN)[0].get_attribute('src')