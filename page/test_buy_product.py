import time

import pytest
from selenium import webdriver

from page.backet_page import basket_page
from page.clothe_page import clothe_page
from page.main_page import main_page
from page.electronics import digital_goods_page

@pytest.mark.run(order=1) #Фикстура для настройки теста, выставление очереди
def test_select_product(set_up):
    driver = webdriver.Chrome()
    driver.maximize_window() # Инициализация страниц
    mp = main_page(driver)
    mp.select_main_menu()
    cl = clothe_page(driver)
    cl.clothe_search()
    bp = basket_page(driver)
    bp.payment()

@pytest.mark.run(order=2) #Фикстура для настройки теста, выставление очереди
def test_select_product_2(set_up_2):
    driver = webdriver.Chrome()
    driver.maximize_window() # Инициализация страниц
    dg = digital_goods_page(driver)
    dg.choose_product()



