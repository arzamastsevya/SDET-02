import unittest
from yandex_page import yandex_page
from yandex_image_page import yandex_image_page
from yandex_image_search_page import yandex_image_search_page
from config import test_config


class test_002(unittest.TestCase):

    URL = test_config.server_name
    browser = test_config.browser
   
    def setUp(self):

        self.yandex_page = yandex_page(self.browser, self.URL)
        self.yandex_image_page = yandex_image_page(self.browser, self.URL)
        self.yandex_image_search_page = yandex_image_search_page(self.browser, self.URL)

    def test_case_002(self):

        self.yandex_page.goto_site()
        self.yandex_page.images_href_click()

        self.browser.switch_to.window(self.browser.window_handles[1])

        category = self.yandex_image_page.get_image_category_name()

        assert self.browser.current_url.find(self.URL+"images/?")==0, f"\"{self.URL}images/\" not current URL {self.browser.current_url}"

        self.yandex_image_page.image_categories_click()

        assert category in self.yandex_image_search_page.get_main_input_text(), "Image category not in search input"
        assert "Картинки" in self.yandex_image_search_page.get_active_tab(), "Images not active tab"

        self.yandex_image_search_page.image_1st_results_click()

        first_image_url_01 = self.yandex_image_search_page.get_image_origin_url() 
        first_image_md5_01 = self.yandex_image_search_page.get_md5_image_screenshot()

        self.yandex_image_search_page.image_next_click()

        assert first_image_url_01 != self.yandex_image_search_page.get_image_origin_url(), "No image change"

        self.yandex_image_search_page.image_previous_click() 

        first_image_md5_02 = self.yandex_image_search_page.get_md5_image_screenshot()
        first_image_url_02 = self.yandex_image_search_page.get_image_origin_url()

        assert first_image_md5_01 == first_image_md5_02, f"Images md5 mismatch {first_image_url_01}, {first_image_url_02}"
        assert first_image_url_01 == first_image_url_02, f"Images URL mismatch {first_image_url_01}\n{first_image_url_02}"
        

    def tearDown(self):

        self.browser.quit()

if __name__ == "__main__":
    unittest.main()