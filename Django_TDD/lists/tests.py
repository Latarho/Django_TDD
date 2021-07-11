from django.test import TestCase
from lists.models import Item


class ItemModelTest(TestCase):
    """Тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """Тест сохранения и получения элементов списка"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_home_page_returns_correct_html(self):
        """Тест: Домашняя страница возвращает правильный html"""
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_uses_home_template(self):
        """Тест: Используется шаблон home_page"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """Тест: Можно сохранить post-запрос"""
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

    def test_only_saves_items_when_necessary(self):
        """Тест: Сохраняет элементы, только когда нужно"""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
