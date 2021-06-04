from django.test import TestCase


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
