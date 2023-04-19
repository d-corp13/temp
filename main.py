import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class HomePage:
    TITLE = "Официальный сайт компании ООО ССЗ Лисма | Лампы и светильники Лисма"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://lisma.su/")

    def is_title_correct(self):
        return self.driver.title == self.TITLE

    def get_url(self):
        return self.driver.current_url


    PRESS_CZENTR_LINK = (By.XPATH, '/html/body/nav/ul/li[6]/a')
    PRESS_CZENTR_URL = "https://lisma.su/press-tsentr/index.html"
    PRESS_CZENTR_TITLE = "Новости ООО \"ССЗ Лисма\""

    def click_press_czentr_link(self):
        pc = self.driver.find_element(*self.PRESS_CZENTR_LINK)
        pc.click()

    def is_press_czentr_page_opened(self):
        return self.driver.current_url == self.PRESS_CZENTR_URL

    def is_press_czentr_title_correct(self):
        return self.driver.title == self.PRESS_CZENTR_TITLE


    KONTAKTYI_LINK = (By.XPATH, '/html/body/nav/ul/li[7]/a')
    KONTAKTYI_URL = "https://lisma.su/kontakty/index.html"

    def click_kontaktyi_link(self):
        pc = self.driver.find_element(*self.KONTAKTYI_LINK)
        pc.click()

    def is_kontaktyi_page_opened(self):
        return self.get_url() == self.KONTAKTYI_URL


    LANGUAGE = "en/"
    LANGUAGE_LINK = (By.XPATH, '/html/body/div[1]/div/div/a[1]')

    def click_language_link(self):
        pc = self.driver.find_element(*self.LANGUAGE_LINK)
        pc.click()

    def get_en_link(self):
        return "https://lisma.su/en/"

    def is_language_en(self):
        return self.get_en_link() == self.driver.current_url


    SEARCH = (By.ID, "search")
    search_text = "Стратегия развития"
    LOUPE = (By.XPATH, '/html/body/div[1]/div/form/input[3]')
    SEARCH_URL = "https://lisma.su/rezultatyi-poiska.html?search=%D0%A1%D1%82%D1%80%D0%B0%D1%82%D0%B5%D0%B3%D0%B8%D1%8F+%D1%80%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D1%8F&id=697"

    def write_search_text(self, search_text):
        element = self.driver.find_element(*self.SEARCH)
        element.send_keys(search_text)

    def click_search(self):
        pc = self.driver.find_element(*self.LOUPE)
        pc.click()

    def is_search_success(self):
        return self.driver.current_url == self.SEARCH_URL

    LAMP_LINK = (By.XPATH, "/html/body/div[3]/div[1]/a[3]/span/span[1]")
    LAMP_SPAN_TEXT = "Лампы"

    def get_text_from_span(self):
        pc = self.driver.find_element(*self.LAMP_LINK)
        return pc.get_attribute('innerHTML')

    def is_true_span_text(self):
        return self.get_text_from_span() == self.LAMP_SPAN_TEXT


class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://lisma.su/")

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_title(self):
        home_page = HomePage(self.driver)
        assert home_page.is_title_correct()

    # def test_PRESS_CZENTR(self):
    #     home_page = HomePage(self.driver)
    #     home_page.click_press_czentr_link()
    #     assert home_page.is_press_czentr_page_opened()

    def test_press_czentr_title(self):
        home_page = HomePage(self.driver)
        home_page.click_press_czentr_link()
        assert home_page.is_press_czentr_title_correct()

    def test_language(self):
        home_page = HomePage(self.driver)
        # en = f"{self.driver.current_url}en/"
        home_page.click_language_link()
        assert home_page.is_language_en()

    def test_search(self):
        home_page = HomePage(self.driver)
        home_page.write_search_text("Стратегия развития")
        home_page.click_search()
        assert home_page.is_search_success()

    def test_span_text(self):
        home_page = HomePage(self.driver)
        home_page.get_text_from_span()
        return home_page.is_true_span_text()

    # def test_kontaktyi(self):
    #     home_page = HomePage(self.driver)
    #     home_page.click_kontaktyi_link()
    #     print(home_page.get_url())
    #     assert home_page.is_kontaktyi_page_opened()


if __name__ == '__main__':
    unittest.main()
