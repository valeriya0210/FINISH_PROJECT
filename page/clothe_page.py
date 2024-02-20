import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains

from utilities.logger import Logger


class clothe_page(Base): #Создание класса потомка

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS
    price = "//*[@id='filters']/div/div/div[2]/ul/li[1]/div/div[2]/div/div[2]/div/div/div[2]"
    height = "//div[@class='filter-checkbox--label'][normalize-space()='86']"
    season = "//div[@class='filter-checkbox--label'][normalize-space()='С капюшоном']"
    mat = "//div[@class='filter-checkbox--label'][normalize-space()='Флис']"
    card = "//*[@id='category-products']/div[1]/div/div/div[2]/div[4]/button"
    size_in_card = "//div[@data-test-id='item__sku' and contains(@data-tooltip, '86')]"
    cart = "//*[@id='product-info']/div[2]/div[6]/div/div/div[1]"
    word = "//div[@id='cart']/h1/span[1]"
    cart_button = "//a[@id='cart-button']"

    #GETTERS
    def get_price(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.price)))
    def get_height(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.height)))
    def get_season(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.season)))
    def get_mat(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.mat)))
    def get_card(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.card)))
    def get_size_in_card(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.size_in_card)))
    def get_cart(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_word(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.word)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    #ACTIONS
    def move_filters(self):
        actions = ActionChains(self.driver)
        price_element = self.get_price()
        actions.click_and_hold(price_element).move_by_offset(-30, 0).release().perform()
        print('Filter price move')

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 500)")

    def click_height(self):
        self.get_height().click()
        print('Click height')

    def click_season(self):
        self.get_season().click()
        print('Click season')

    def click_mat(self):
        self.get_mat().click()
        print('Click mat')

    def click_card(self):
        self.get_card().click()
        print('Click card')

    def click_size_in_card(self):
        self.get_size_in_card().click()
        print('Click size card')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart')
    def click_cart_button(self):
        self.get_cart_button().click()
        print('Click cart')

    #METHOD
    def clothe_search(self):
        current_url = self.driver.current_url  # Получаем текущий URL
        Logger.add_start_step(method="clothe_search")  # Добавляем запись о начале шага
        self.move_filters() #Двигаем бегунок для корректировки цены
        self.scroll() #Скроллим страницу вниз
        self.click_height() #Ставим чек-бокс на фильтре - рост
        self.click_season() #Ставим чек-бокс на фильтре - капюшон
        self.scroll() #Скроллим страницу вниз
        self.click_mat() #Ставим чек-бокс на фильтре - материал
        self.click_card() #Пееходим в карточку
        self.click_size_in_card() #Устанавливаем размер
        self.click_cart() #Добавляем в корзину
        self.click_cart_button() #Переходим в корзину
        self.assert_word(self.get_word(), 'Ваша корзина,') #Проверяем наличие слова методом assert
        self.get_screenshot()  # Делаем скриншот
        Logger.add_end_step(url=self.driver.current_url, method="clothe_search")  # Добавляем запись о завершении шага





