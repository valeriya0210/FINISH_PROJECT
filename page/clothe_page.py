import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class clothe_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.driver.get(self.url)

    #LOCATORS
    search_input = "//input[@id='searchInput']"
    btn_search = "//button[@id='applySearchBtn']"
    dropdown_filter = "//button[@class='dropdown-filter__btn dropdown-filter__btn--all']"
    min_price = "//input[@name='startN']"
    max_price = "//input[@name='endN']"
    show = "//button[@class='filters-desktop__btn-main btn-main']"

    #GETTERS
    def get_search_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_input)))

    def get_btn_search(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_search)))

    def get_dropdown_filter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_filter)))

    def get_min_price(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_show(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.show)))

    #ACTIONS
    def input_search_input(self):
        self.get_search_input().send_keys('Куртки')
        print('Input search')

    def click_btn_search(self):
        self.get_btn_search().click()
        print('Click button search')

    def click_dropdown_filter(self):
        self.get_dropdown_filter().click()
        print('Click dropdown filter')

    def click_min_price(self):
        self.get_min_price().click()
        print('Input min_price')

    def input_min_price(self):
        self.get_min_price().send_keys('5000')
        print('Input min_price')

    def click_max_price(self):
        self.get_max_price().click()
        print('Input min_price')

    def input_max_price(self):
        self.get_max_price().send_keys('10000')
        print('Input max_price')

    def click_show(self):
        self.get_show().click()
        print('Show')

    def scrol3(self):
        modal = self.driver.find_element(By.XPATH, "//div[@class='filters-desktop__list j-filters-list']")
        self.driver.execute_script("arguments[0].scrollTop = 1500;", modal)

    #METHOD
    def clothe_search(self):
        self.get_current_url()
        self.input_search_input()
        time.sleep(5)
        self.click_btn_search()
        time.sleep(5)
        self.click_dropdown_filter()
        time.sleep(2)
        time.sleep(2)
        self.click_min_price()
        min_price_input = self.get_min_price()  # Получаем элемент поля ввода минимальной цены
        min_price_input.clear()  # Очищаем поле ввода
        time.sleep(2)
        self.input_min_price()

        self.click_max_price()
        max_price_input = self.get_max_price()
        max_price_input.clear()
        time.sleep(2)
        self.input_max_price()
        self.click_show()
        time.sleep(2)




