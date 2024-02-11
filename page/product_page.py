import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS
    search_input_2 = "//input[@id='searchInput']"
    btn_search_2 = "//button[@id='applySearchBtn']"
    size = '//label[@class="j-size sizes-list__button"]/span[@class="sizes-list__size"][contains(., "L (42/48)")]'
    basket = "//div[contains(@class, 'product-page__aside')]//span[contains(text(),'в корзину')]"

    #GETTERS
    def get_search_input_2(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.search_input_2)))

    def get_btn_search_2(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.btn_search_2)))

    def get_size(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.size)))

    def get_basket(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.basket)))

    #ACTIONS
    def click_search_input_2(self):
        self.get_search_input_2().click()
        print('Click search input 2')

    def input_search_input_2(self):
        search_input = self.get_search_input_2()
        search_input.clear()
        search_input.send_keys('154669457')
        print('Input art')

    def click_btn_search_2(self):
        self.get_btn_search_2().click()
        print('Click btn search 2')

    def click_scroll_4(self):
        self.driver.execute_script("window.scrollTo(0, 50)")

    def click_size(self):
        self.get_size().click()
        print('Click size')

    def click_basket(self):
        self.get_basket().click()
        print('Click basket')

    # METHOD
    def choose_product(self):
        self.get_current_url()
        self.click_search_input_2()
        time.sleep(2)
        self.input_search_input_2()
        time.sleep(2)
        self.click_btn_search_2()
        time.sleep(2)
        self.click_size()
        time.sleep(5)
        self.click_scroll_4()
        time.sleep(5)
        self.click_basket()
        time.sleep(2)



