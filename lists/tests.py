from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePage(TestCase):
    """Тест домашней страницы"""

    def test_root_url_resolves_to_home_page_view(self):
        """тест: корневой url преобразуется в предствление
        домашней страницы"""
        found = resolve(r"/")
        self.assertEqual(found.func, home_page)
