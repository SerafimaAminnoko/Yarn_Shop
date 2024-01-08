from django.test import SimpleTestCase


class UrlTestCase(SimpleTestCase):
    def main_page(self):
        assert 1 == 2