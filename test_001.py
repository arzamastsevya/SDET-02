import unittest
from yandex_page import yandex_page
from yandex_search_results_page import yandex_search_results_page
from config import test_config


class test_001(unittest.TestCase):

    URL = test_config.server_name
    browser = test_config.browser

    def setUp(self):

        self.yandex_page = yandex_page(self.browser, self.URL)
        self.yandex_search_results_page = yandex_search_results_page(self.browser, self.URL)

    def test_case_001(self):

        self.yandex_page.goto_site()     
        self.yandex_page.input_send_word("Тензор")
        self.yandex_page.get_suggest()
        self.yandex_page.input_send_ENTER()

        href_list = self.yandex_search_results_page.get_href_URLs()  
        for i in href_list[:4]:
            assert href_list[href_list.index(i)].find("https://tensor.ru/")==0, f"No \"tensor.ru\" link in {href_list.index(i)+1}th search result"

    def tearDown(self):

        self.browser.quit()

if __name__ == "__main__":
    unittest.main()