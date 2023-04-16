import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:

    TITLE = "Официальный сайт компании ООО ССЗ Лисма | Лампы и светильники Лисма"

    LANGUAGE = "en/"
    LANGUAGE_LINK = (By.XPATH, '/html/body/div[1]/div/div/a[1]')

    PRESS_CZENTR_LINK = (By.XPATH, '/html/body/nav/ul/li[6]/a')
    PRESS_CZENTR_URL = "https://lisma.su/press-tsentr/index.html"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://lisma.su/")

    def is_title_correct(self):
        return self.driver.title == self.TITLE


    def set_en_lang(self, driver):
        self.driver = driver
        self.driver.get(f"{self.driver.current_url}{LANGUAGE}")



    def get_url(self):
        return self.driver.current_url

    def click_PRESS_CZENTR_LINK(self):
        pc = self.driver.find_element(*self.PRESS_CZENTR_LINK)
        pc.click()

    def click_language_LINK(self):
        pc = self.driver.find_element(*self.LANGUAGE_LINK)
        pc.click()

    def is_PRESS_CZENTR_page_opened(self):
        return self.driver.current_url == self.PRESS_CZENTR_URL



class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://lisma.su/")

    def tearDown(self):
        self.driver.quit()


    def test_title(self):
        home_page = HomePage(self.driver)
        assert home_page.is_title_correct()


    def test_language(self):
        home_page = HomePage(self.driver)
        en = f"{self.driver.current_url}en/"
        home_page.click_language_LINK()

        assert en == home_page.driver.current_url



if __name__ == '__main__':
    unittest.main()



# import unittest
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import pytest
#
# class PythonSearchTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://www.python.org")
#         time.sleep(2)
#
#     def test_title(self):
#         self.assertEqual(self.driver.title, "Welcome to Python.org")
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main()
