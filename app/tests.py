"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the Домашняя страница page."""
        response = self.client.get('/')
        self.assertContains(response, 'Домашняя страница', 1, 200)

    def test_contact(self):
        """Tests the Контакты page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Контакты', 3, 200)

    def test_about(self):
        """Tests the О нас page."""
        response = self.client.get('/about')
        self.assertContains(response, 'О нас', 3, 200)
    def test_links(self):
        """Tests the спонсоры  page."""
        response = self.client.get('/links')
        self.assertContains(response, 'спонсоры', 3, 200)
