from decimal import Decimal

from django.db.models import Q, Min, Max, Avg
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from unicodedata import decimal

from shop.filters import YarnFilter
from shop.models import *


class Filters:
    def get_minMaxPrice(self):
        return SubCategory.objects.aggregate(Min('price'), Max('price'), Avg('price'))

    def get_colors(self):
        return Color.objects.all()

    def get_producers(self):
        return Producer.objects.all()

    def get_countries(self):
        return Country.objects.all()


class ProductList(Filters, ListView):
    model = Yarn
    queryset = Yarn.objects.all()
    template_name = 'shop/main.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minMaxPrice'] = Filters.get_minMaxPrice(self)
        return context


class CategoryProductList(Filters, ListView):
    model = Yarn
    template_name = 'shop/subcategories.html'

    def get_queryset(self):
        return Yarn.objects.filter(cat__url=self.kwargs['cat_slug'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory_list'] = SubCategory.objects.filter(cat__url=self.kwargs['cat_slug'])
        context['minMaxPrice'] = Filters.get_minMaxPrice(self)
        return context


class SubCategoryProductList(Filters, ListView):
    model = Yarn
    template_name = 'shop/subcategory_products.html'

    def get_queryset(self):
        return Yarn.objects.filter(subcat__url=self.kwargs['subcat_slug'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.get(url=self.kwargs['subcat_slug'])
        context['minMaxPrice'] = Filters.get_minMaxPrice(self)
        return context




class FilterYarnList(Filters, ListView,):
    template_name = 'shop/main.html'

    def get_queryset(self):
        FilterPrice = self.request.GET['FilterPrice']
        availability = self.request.GET.get('available', True)
        absence = self.request.GET.get('available')

        q = Q()
        if "country" in self.request.GET:
            q = Q(count__in=self.request.GET.getlist("country"))
        if "producer" in self.request.GET:
            q &= Q(prod__in=self.request.GET.getlist("producer"))
        if "color" in self.request.GET:
            q &= Q(col__in=self.request.GET.getlist("color"))
        if "price" in self.request.GET:
            q &= Q(subcat__price__lte=FilterPrice)
        if "available" in self.request.GET:
            q &= Q(availability=availability)
        if "available" in self.request.GET:
            q &= Q(availability=absence)

        queryset = Yarn.objects.filter(q).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minMaxPrice'] = Filters.get_minMaxPrice(self)
        return context



class ProductDetail(Filters, DetailView):
    model = Yarn
    template_name = 'shop/product_detail.html'

    def get_object(self, queryset=None):
        return Yarn.objects.get(url=self.kwargs['product_slug'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minMaxPrice'] = Filters.get_minMaxPrice(self)
        return context

