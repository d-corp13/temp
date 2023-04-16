import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    NEW_ORDER_LINK = (By.XPATH, '//*[@id="navigation"]/li[5]/a')
    PILLS_TAB = (By.XPATH, '//*[@id="pills-tab"]')
    TITLE = "hlebrm"
    CATALOG_LINK = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div/div/a')
    CATALOG_URL = "http://hlebrm.ru/catalog.html"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://hlebrm.ru/")

    def is_title_correct(self):
        return self.driver.title == self.TITLE

    def navigate_to_new_order(self):
        self.driver.find_element(*self.NEW_ORDER_LINK).click()

    def is_pills_tab_displayed(self):
        pills_tab = self.driver.find_element(*self.PILLS_TAB)
        return 'Торты' in pills_tab.text and 'Хлеб' in pills_tab.text and 'Пирожные' in pills_tab.text and 'Выпечка' in pills_tab.text

    def get_url(self):
        return self.driver.current_url

    def click_catalog_link(self):
        catalog_link = self.driver.find_element(*self.CATALOG_LINK)
        catalog_link.click()

    def is_catalog_page_opened(self):
        return self.driver.current_url == self.CATALOG_URL


class NewOrderPage:
    NAME_FIELD = (By.XPATH, '//*[@id="form4Example1"]')
    PHONE_FIELD = (By.XPATH, '//*[@id="form4Example2"]')
    SUBMIT_BUTTON = (By.XPATH, '/html/body/div[2]/div/form/button')

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        name_field = self.driver.find_element(*self.NAME_FIELD)
        name_field.click()
        name_field.clear()
        name_field.send_keys(name)

    def set_phone_number(self, phone_number):
        phone_field = self.driver.find_element(*self.PHONE_FIELD)
        phone_field.click()
        phone_field.clear()
        phone_field.send_keys(phone_number)

    def submit_order(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_url(self):
        return self.driver.current_url


class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://hlebrm.ru/")

    def tearDown(self):
        self.driver.quit()

    def test_new_order(self):
        home_page = HomePage(self.driver)
        home_page.navigate_to_new_order()

        new_order_page = NewOrderPage(self.driver)
        self.assertEqual(new_order_page.get_url(), "http://hlebrm.ru/new-order/")

        new_order_page.set_name("Name")
        new_order_page.set_phone_number("Phone number")
        new_order_page.submit_order()

        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_url(), "http://hlebrm.ru/")

    def test_pills(self):
        home_page = HomePage(self.driver)
        assert home_page.is_pills_tab_displayed()

    def test_title(self):
        home_page = HomePage(self.driver)
        assert home_page.is_title_correct()

    def test_tilte(self):
        home_page = HomePage(self.driver)
        assert home_page.is_title_correct()

    def test_catalog(self):
        home_page = HomePage(self.driver)
        home_page.click_catalog_link()
        assert home_page.is_catalog_page_opened()


if __name__ == '__main__':
    unittest.main()
