from django.test import SimpleTestCase
from django.urls import reverse, resolve

from shop.views import ProductList


class UrlTestCase(SimpleTestCase):
    def main_page(self):
        assert 2 == 2
#        url = reverse('')
#        self.assertEquals(resolve(url).func.view_class, ProductList)