# Create your views here.
from django.db.models import Q
from django.views.generic import ListView, DetailView
from shop.forms import YarnFilterForm
from shop.models import *
from shop.utils import DataMixin


class ProductList(DataMixin, ListView):
    paginate_by = 3
    template_name = 'shop/main.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        form = YarnFilterForm(self.request.GET)
        yarn = Yarn.objects.all()
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)
        context['paginate_by'] = f"paginate_by={self.request.GET.get('paginate_by', self.paginate_by)}&"
        context['count'] = Yarn.objects.filter(availability=True).count()
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CategoryProductList(DataMixin, ListView):
    paginate_by = 16
    template_name = 'shop/category_product_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        form = YarnFilterForm(self.request.GET)
        yarn = Yarn.objects.filter(cat__url=self.kwargs['cat_slug']).order_by('name')
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_by'] = f"paginate_by={self.request.GET.get('paginate_by', self.paginate_by)}&"
        context['count'] = Yarn.objects.filter(cat__url=self.kwargs['cat_slug'], availability=True).count()
        context['subcategory_list'] = SubCategory.objects.filter(cat__url=self.kwargs['cat_slug'])
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SubCategoryProductList(DataMixin, ListView):
    paginate_by = 16
    template_name = 'shop/subcategory_product_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        form = YarnFilterForm(self.request.GET)
        yarn = Yarn.objects.filter(subcat__url=self.kwargs['subcat_slug']).order_by('name')
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_by'] = f"paginate_by={self.request.GET.get('paginate_by', self.paginate_by)}&"
        context['count'] = Yarn.objects.filter(subcat__url=self.kwargs['subcat_slug'], availability=True).count()
        context['subcategory_object'] = SubCategory.objects.get(url=self.kwargs['subcat_slug'])
        c_def = self.get_user_context()
        context = (dict(list(context.items()) + list(c_def.items())))
        return context


class FilterProductList(DataMixin, ListView,):
    paginate_by = 16
    template_name = 'shop/search-filter_product_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        q = Q()
        if "country" in self.request.GET:
            q = Q(count__in=self.request.GET.getlist("country"))
        if "producer" in self.request.GET:
            q &= Q(prod__in=self.request.GET.getlist("producer"))
        if "color" in self.request.GET:
            q &= Q(col__in=self.request.GET.getlist("color"))
        if "max-price" in self.request.GET:
            q &= Q(subcat__price__lte=self.request.GET['max-price'])
        if "available" in self.request.GET:
            q &= Q(availability=True)

        form = YarnFilterForm(self.request.GET)
        yarn = Yarn.objects.filter(q).distinct()
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['price'] = f'max-price={self.request.GET["max-price"]}&'
        context['producer'] = ''.join([f'producer={x}&' for x in self.request.GET.getlist("producer")])
        context['country'] = ''.join([f'country={x}&' for x in self.request.GET.getlist("country")])
        context['color'] = ''.join([f'color={x}&' for x in self.request.GET.getlist("color")])
        context['available'] = ''.join([f'available={self.request.GET.get("available", True)}&'])
        context['paginate_by'] = f'paginate_by={self.request.GET.get("paginate_by", self.paginate_by)}&'
        context['count'] = Yarn.objects.filter(availability=True).count()
        c_def = self.get_user_context()
        context = (dict(list(context.items()) + list(c_def.items())))
        return context


class SearchProductList(DataMixin, ListView):
    paginate_by = 16
    template_name = 'shop/search-filter_product_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        form = YarnFilterForm(self.request.GET)
        yarn = Yarn.objects.filter(name__icontains=self.request.GET.get('query')).order_by('name')
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_by'] = f'paginate_by={self.request.GET.get("paginate_by", self.paginate_by)}&'
        context['count'] = Yarn.objects.filter(availability=True).count()
        context['q'] = f'query={self.request.GET.get("query")}&'
        c_def = self.get_user_context()
        context = (dict(list(context.items()) + list(c_def.items())))
        return context


class ProductDetail(DetailView):
    model = Yarn
    template_name = 'shop/product_detail.html'

    def get_object(self, queryset=None):
        return Yarn.objects.get(url=self.kwargs['product_slug'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['yarns'] = Yarn.objects.all()
        return context





