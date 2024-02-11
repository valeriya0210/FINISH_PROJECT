import time
from selenium import webdriver

from page.backet_page import basket_page
from page.clothe_page import clothe_page
from page.digital_goods_page import digital_goods_page
from page.main_page import main_page
from page.product_page import product_page


def test_select_product(set_up):
    driver = webdriver.Chrome()
    driver.maximize_window()
    mp = main_page(driver)
    mp.select_main_menu()
    dg = digital_goods_page(driver)
    dg.select_product()
    cl = clothe_page(driver)
    cl.clothe_search()
    pp = product_page(driver)
    pp.choose_product()
    bp = basket_page(driver)
    bp.payment()

    time.sleep(5)



