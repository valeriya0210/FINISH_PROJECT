import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class digital_goods_page(Base): #Создание класса потомка

    url = 'https://kazanexpress.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(self.url)

    #LOCATORS
    electronic = "//a[@class='ui-link category__body slightly transparent' and contains(text(), 'Электроника')]"
    filt = "//*[@id='category-content']/div[1]/div[2]/div/div[2]/span[2]"
    price = "//input[@data-test-id='input__max-price']"
    rating = "//*[@id='category-content']/div[1]/div[2]/div/div[1]/ul/li[4]"
    case = "//div[@id='category-products']/div[1]"
    next_photo = "//div[@data-test-id='button__next-photo']"
    favorites = "//div[@data-test-id='button__add-to-favorites']"

    #GETTERS
    def get_electronic(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.electronic)))

    def get_filt(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.filt)))

    def get_input(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_rating(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.rating)))

    def get_case(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.case)))

    def get_next_photo(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.next_photo)))

    def get_favorites(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.favorites)))


    #ACTIONS
    def click_electronic(self):
        self.get_electronic().click()
        print('Click electronic')

    def scrol(self):
        self.driver.execute_script("window.scrollTo(0, 500)")

    def click_filt(self):
        self.get_filt().click()
        print('Click filt')

    def click_rating(self):
        self.get_rating().click()
        print('Click rating')

    def input_price(self):
        self.get_input().send_keys('5000')
        print('Price input')

    def enter_price(self):
        self.get_input().send_keys(Keys.RETURN)
        print('Price enter')

    def click_case(self):
        self.get_case().click()
        print('Click case')

    def click_next_photo(self):
        self.get_next_photo().click()
        print('Click next photo')

    def click_favorites(self):
        self.get_favorites().click()
        print('Click favorites')

    #Методы
    def choose_product(self):
        current_url = self.driver.current_url  # Получаем текущий URL
        Logger.add_start_step(method="choose_product")  # Добавляем запись о начале шага
        self.get_current_url() #Получаем текущую ссылку
        self.click_electronic() #Кликаем на категорию Электроника
        self.click_filt() #Кликаем на филтр
        self.click_rating() #Кликаем на дроп даун Рейтинг
        self.scrol() #Скролл вниз
        self.input_price() #Вводит значение для поля Цена
        self.enter_price()
        self.click_case() #Переходим в карточку
        self.click_next_photo() #Нажимаем на кнопку следующее фото в карусели
        self.click_favorites() #Добавляем в избранное
        self.get_screenshot() #Делаем скриншот
        Logger.add_end_step(url=self.driver.current_url, method="choose_product")  # Добавляем запись о завершении шага
