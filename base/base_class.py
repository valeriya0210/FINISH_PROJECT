import datetime


class Base(): #Содание базового класса
    def __init__(self, driver): #Инициализация браузера
        self.driver = driver

    """Get current url"""
    def get_current_url(self): #Метод для получения текущей ссылки
        current_url = self.driver.current_url
        print(current_url)

    """Assert word"""
    def assert_word(self, word, result): #Проверка, что текст элемента соответствует ожидаемому результату.
        value_word = word.text
        assert value_word == result
        print('Assert OK')

    """Screenshot"""

    def get_screenshot(self): #Сохранение скриншота с временным штампом в имени файла.
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = 'screen' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\pythonProject1\\base\\screenshot' + name_screen)













