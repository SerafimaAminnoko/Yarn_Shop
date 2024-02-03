from http import client

from django.test import TestCase, Client
from django.urls import reverse, resolve

from shop.views import *


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.product_list_url = reverse('main')
        self.category_product_list_url = reverse('category', args=['cat_slug'])

    def test_view_product_list(self):
        response = self.client.get(self.product_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/main.html')

    def test_view_category_product_list(self):

        response = self.client.get(self.category_product_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/category_product_list.html')



