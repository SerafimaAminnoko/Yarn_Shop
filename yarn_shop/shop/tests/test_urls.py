from django.test import SimpleTestCase
from django.urls import reverse, resolve

from shop.views import ProductList


class UrlTestCase(SimpleTestCase):
    def main_page(self):
        url = reverse('')
        print(url)
        self.assertEquals(resolve(url).func.view_class, ProductList)