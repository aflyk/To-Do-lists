from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest


class NewVisitorTest(unittest.TestCase):
    """тест нового посетителя"""

    def setUp(self):
        """установка"""
        options = Options()
        options.binary_location =r"C:\Program Files\Mozilla Firefox\firefox.exe"
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self) -> None:
        """демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест можно начать список и получить его позже"""
        # Эдит слышала про крутое нвоое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о списках
        # неотложных дел
        self.assertIn("ToDo", self.browser.title)
        self.fail("Закончить тест!")
        # Ей сразу же предлагается ввести элемент списка


        # Она набирает в текстовом поле "купить павлиньи перья"(ее хобби -
        # вязание рыболовных мушек)

        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка

        # тесктовое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев "
        # (Эдит очень методична)

        # Страница снова обновляется, и тепеерь показывает оба элемента ее списка

        # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
        # сайт сгенерировал для нее уникальный URL-адресс - об этом
        # выводится небольшой текст с объяснениями.

        # Она посещает этот URL-адресс - ее список по-прежнему там.

        # Удовлетворенная, она снова ложится спать

if __name__ == "__main__":
    unittest.main(warnings="ignore")

