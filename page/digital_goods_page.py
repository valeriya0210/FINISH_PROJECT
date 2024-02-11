import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class digital_goods_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS
    fil_price = '//*[@id="body"]/div/div/div/div[1]/div/div/div/a[2]'
    course_cart = '//*[@id="o_132303"]/div/div[2]/div[2]/button[1]/div'
    word = '//*[@id="body"]/div[2]/div/div/div/div/h1/span/em'

    #GETTERS
    def get_fil_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fil_price)))

    def get_course_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.course_cart)))

    def get_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.word)))

    #ACTIONS
    def click_fil_price(self):
        self.get_fil_price().click()
        print('Click course cart')

    def scrol2(self):
        self.driver.execute_script("window.scrollTo(0, 300)")

    def click_course_cart(self):
        self.get_course_cart().click()
        print('Click course cart')

    #METHOD
    def select_product(self):
        self.get_current_url()
        time.sleep(2)
        self.click_fil_price()
        time.sleep(2)
        self.scrol2()
        time.sleep(2)
        self.click_course_cart()
        time.sleep(2)
        self.assert_word(self.get_word(), 'Wildberries Цифровой')
        time.sleep(2)
        self.driver.back()
        self.driver.back()
        time.sleep(5)

