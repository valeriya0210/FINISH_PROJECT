#Главная страница - в поиске вбиваем значение и переходим на следующую страницу с выдачей товара.
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class main_page(Base): #Создание класса потомка
    url = 'https://kazanexpress.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(self.url)  # Добавляем эту строку для перехода на страницу

    #LOCATORS
    search_input = "//input[@data-test-id='input__search']"
    btn_search = "//button[@data-test-id='button__search']"

    #GETTERS
    def get_search_input(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.search_input)))

    def get_btn_search(self):
        return WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, self.btn_search)))

    #ACTIONS
    def click_search_input(self):
        self.get_search_input().click()
        print('Click search input')

    def input_search_input(self):
        self.get_search_input().send_keys('Куртки')
        print('Input search')

    def click_btn_search(self):
        self.get_btn_search().click()
        print('Click btn search')

    #METHOD
    def select_main_menu(self):
        current_url = self.driver.current_url  # Получаем текущий URL
        Logger.add_start_step(method="select_main_menu")  # Добавляем запись о начале шага
        self.click_search_input()  # Нажимаем на строку поиска на главной странице
        self.input_search_input()  # Вводим значение "Куртки" в строку поиска
        self.click_btn_search()  # Нажимаем на кнопку поиска
        self.get_screenshot()  # Делаем скриншот
        Logger.add_end_step(url=self.driver.current_url, method="select_main_menu")  # Добавляем запись о завершении шага




