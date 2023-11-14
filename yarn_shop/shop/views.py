from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from shop.models import *


class ProductList(ListView):
    model = Yarn
    queryset = Yarn.objects.all()
    template_name = 'shop/main.html'


class CategoryProductList(ListView):
    model = Yarn
    template_name = 'shop/main.html'

    def get_queryset(self):
        return Yarn.objects.filter(cat__url=self.kwargs['cat_slug'])
