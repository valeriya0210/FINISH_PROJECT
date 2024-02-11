import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from faker import Faker

class basket_page(Base):

    faker = Faker()
    random = faker.random_number(digits=10)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.driver.get(self.url)

    #LOCATORS
    go_to_bask = '//a[@data-wba-header-name="Cart"]'
    word = '//p[@class="b-top__total line"]/span'
    pay = '//*[@id="app"]/div[4]/div/div[1]/form/div[1]/div[3]/div[1]/p/a'
    number = '//input[@type="text"]'
    code = '//button[@id="requestCode"]'

    #GETTERS
    def get_go_to_bask(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_bask)))

    def get_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.word)))

    def get_pay(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pay)))

    def get_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.number)))

    def get_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.code)))

    #ACTIONS
    def click_go_to_bask(self):
        self.get_go_to_bask().click()
        print('Click go_to_bask')

    def click_pay(self):
        self.get_pay().click()
        print('Click pay')

    def input_number(self):
        random = self.faker.random_number(digits=11)
        self.get_number().send_keys(str(random))
        print('Input number')

    def click_code(self):
        self.get_code().click()
        print('Click code')


    # METHOD
    def payment(self):
        self.get_current_url()
        self.click_go_to_bask()
        time.sleep(3)
        self.assert_word(self.get_word(), 'Итого')
        time.sleep(3)
        self.click_pay()
        time.sleep(3)
        self.input_number()
        time.sleep(3)
        # self.click_code()
        # time.sleep(3)

