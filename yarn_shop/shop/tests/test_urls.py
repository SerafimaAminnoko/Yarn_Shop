from django.test import TestCase
from django.urls import reverse, resolve

from shop.views import *


class UrlsTestCase(TestCase):
    def test_url_product_list(self):
        url = reverse('main')
        self.assertEquals(resolve(url).func.view_class, YarnList)

    def test_url_category_product_list(self):
        url = reverse('category', args=['cat_slug'])
        self.assertEquals(resolve(url).func.view_class, CategoryYarnList)

    def test_url_subcategory_product_list(self):
        url = reverse('subcategory', args=['subcat_slug'])
        self.assertEquals(resolve(url).func.view_class, SubCategoryYarnList)

    def test_url_filter_product_list(self):
        url = reverse('filter')
        self.assertEquals(resolve(url).func.view_class, FilterYarnList)

    def test_url_search_product_list(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, SearchYarnList)

    def test_url_product_detail(self):
        url = reverse('product_detail', args=['product_slug'])
        self.assertEquals(resolve(url).func.view_class, YarnDetail)