#Страница корзины, здесь осуществляется переход на страницу оплаты, где мы заполняем основные поля - имя, фамилия, телефон, емэйл, адрес. 
#Далее переходим в личный кабинет и методом faker генерируем случайные значения для поля номер.

import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from faker import Faker

from utilities.logger import Logger

class basket_page(Base): #Создание класса потомка
    def __init__(self, driver):
        super().__init__(driver)

    faker = Faker()
    random = faker.random_number(digits=10)

    #LOCATORS
    number = "//input[@placeholder='000 000-00-00']"
    register = "//*[@id='cart-sum']/div/div[2]/div[5]/button/div"
    courier = "//div[@data-test-id='radio-button__select-cdelivery']"
    street = "//input[@name='street']"
    flat = "//input[@name='flat']"
    comment = "//input[@name='comment']"
    time = "//span[@data-test-id='text__selected-value' and text()='Выберите время']"
    time_choose = "/html/body/div[3]/main/div/div[1]/div/div[2]/div[1]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/ul/li[2]"
    lastname = "//input[@name='lastname']"
    firstname = "//input[@name='firstname']"
    phone = "//input[@name='phone']"
    email = "//input[@name='email']"
    entrance = "//*[@id='signup-button']/div"

    #GETTERS
    def get_entrance(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.entrance)))
    def get_number(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.number)))
    def get_register(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.register)))
    def get_courier(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.courier)))
    def get_street(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.street)))
    def get_flat(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.flat)))
    def get_comment(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.comment)))
    def get_time(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.time)))
    def get_time_choose(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.time_choose)))
    def get_lastname(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.lastname)))
    def get_firstname(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.firstname)))
    def get_phone(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.phone)))
    def get_email(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    #ACTIONS
    def click_entrance(self):
        self.get_entrance().click()
        print('Click entrance')

    def input_number(self):
        random = self.faker.random_number(digits=11)
        self.get_number().send_keys(str(random))
        print('Input number')

    def click_register(self):
        self.get_register().click()
        print('Click register')

    def click_courier(self):
        self.get_courier().click()
        print('Click courier')

    def click_time(self):
        self.get_time().click()
        print('Click time')

    def click_time_choose(self):
        self.get_time_choose().click()
        print('Click time choose')

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 500)")

    def scroll_2(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
    def scroll_3(self):
        self.driver.execute_script("window.scrollTo(0, -1000)")

    def input_street(self):
        street_input = self.get_street()
        street_input.send_keys('ул Казанская, д 33')
        print('Street input')
        street_input.send_keys(Keys.RETURN)

    def input_flat(self):
        flat_input = self.get_flat()
        flat_input.send_keys('35')
        print('Flat input')

    def input_comment(self):
        comment_input = self.get_comment()
        comment_input.send_keys('ПРИВЕТ!')
        print('Comment input')

    def input_lastname(self):
        lastname_input = self.get_lastname()
        lastname_input.send_keys('Иванов')
        print('Lastname input')

    def input_firstname(self):
        firstname_input = self.get_firstname()
        firstname_input.send_keys('Иван')
        print('Firstname input')

    def input_phone(self):
        phone_input = self.get_phone()
        phone_input.send_keys('7 (589) 653-25-89')
        print('Phone input')

    def input_email(self):
        email_input = self.get_email()
        email_input.send_keys('ivanov@mail.ru')
        print('Phone input')

    #METHOD
    def payment(self):
        current_url = self.driver.current_url  # Получаем текущий URL
        Logger.add_start_step(method="payment")  # Добавляем запись о начале шага
        self.get_current_url() #Получаем текущую ссылку
        self.click_register() #Переход на страницу оплаты
        self.click_courier() #Добавление курьерской доставки
        self.scroll() #Скролл вниз
        self.input_street() #Вводим значение для поля Улица
        self.input_flat() #Вводим значение для поля Квартира
        self.input_comment() #Вводим значение для поля Комментарий
        self.click_time() #Нажимаем на поле Время доставки
        self.click_time_choose() #Устанавливаем время доставки
        self.scroll_2() #Скролл вниз
        self.input_lastname() #Вводим значение для поля Фамилия
        self.input_firstname() #Вводим значение для поля Имя
        self.input_phone() #Вводим значение для поля Телефон
        self.input_email() #Вводим значение для поля Емэйл
        self.scroll_3() #Скролл вверх
        self.click_entrance() #Переходим в личный кабинет
        self.input_number() #Генерируем случайно число методом faker
        self.get_screenshot()  # Делаем скриншот
        Logger.add_end_step(url=self.driver.current_url, method="payment")  # Добавляем запись о завершении шага


