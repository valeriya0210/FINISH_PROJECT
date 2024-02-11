import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base

class main_page(Base):
    url = 'https://www.wildberries.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(self.url)  # Добавляем эту строку для перехода на страницу

    #LOCATORS
    menu = '//button[@class="nav-element__burger j-menu-burger-btn j-wba-header-item"]'
    digital_goods = "//a[@class='menu-burger__main-list-link menu-burger__main-list-link--62813']"
    music = '/html/body/div[1]/div[2]/div[3]/div/div[25]/div/div[1]/ul/li[5]/a'

    #GETTERS
    def get_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_digital_goods(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.digital_goods)))

    def get_music(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.music)))


    #ACTIONS
    def click_menu(self):
        self.get_menu().click()
        print('Click product')

    def scrol(self):
        modal = self.driver.find_element(By.XPATH, "//div[@class='menu-burger__main j-menu-burger-main j-menu-active']")
        # self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.execute_script("arguments[0].scrollTop = 500;", modal)

    def move_digital_goods(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_digital_goods()).perform()

    def click_music(self):
        self.get_music().click()
        print('Click music')

    #Методы
    def select_main_menu(self):
        self.get_current_url()
        time.sleep(2)
        self.click_menu()
        time.sleep(2)
        self.scrol()
        time.sleep(2)
        self.move_digital_goods()
        time.sleep(2)
        self.click_music()



