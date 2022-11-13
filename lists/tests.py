from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


class HomePage(TestCase):
    """Тест домашней страницы"""

    def test_root_url_resolves_to_home_page_view(self):
        """тест: корневой url преобразуется в предствление
        домашней страницы"""
        found = resolve(r"/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """тест: домашняя страница возвращает правильный html"""
        requests = HttpRequest()
        response = home_page(requests)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith('<html>'))
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.endswith("</html>"))