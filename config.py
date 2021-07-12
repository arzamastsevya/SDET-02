from selenium import webdriver

class test_config:

    server_name = "https://yandex.ru/"
    browser = webdriver.Firefox()
    browser.set_window_position(0, 0)
    browser.set_window_size(1920, 1080)