from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self):
        """Предусловие"""
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=self.options, executable_path='C:\Drivers\chromedriver.exe')

    def tearDown(self):
        """Постусловие"""
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        # Эдит слышала про крутое новое онлайн-приложение со списком неотложных дел.
        # Она решает оценить его домашнюю страницу
        self.driver.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о списках неотложных дел.
        self.assertIn('To-Do', self.driver.title)
        header_text = self.driver.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.driver.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Она набирает в текстовом поле поле 'Купить павлиньи перья' (ее хобби - вязание рыбловоных мушек)
        inputbox.send_keys('Купить павлиньи перья')

        # Когда она нажимает enter, страница обновляется, и теперь страница содержит
        # "1: Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.driver.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Купить павлиньи перья' for row in rows))

        # Текствое поле по-прежнему приглашает ее добавить еще один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # (Эдит очень методична)

        self.fail('Закончить тест!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
