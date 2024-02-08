# Create your views here.
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from cart.forms import CartAddYarnForm
from shop.forms import YarnOrderingForm
from shop.models import *
from shop.utils import DataMixin


class YarnList(DataMixin, ListView):
    paginate_by = 16
    template_name = 'shop/yarn_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        form = YarnOrderingForm(self.request.GET)
        yarn = Yarn.objects.all().select_related('subcat')
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Yarn.objects.filter(availability=True).count()
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class CategoryYarnList(DataMixin, ListView):
    paginate_by = 16
    template_name = 'shop/category_yarn_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        form = YarnOrderingForm(self.request.GET)
        yarn = Yarn.objects.filter(subcat__cat__url=self.kwargs['cat_slug']).order_by('name').select_related('subcat')
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Yarn.objects.filter(subcat__cat__url=self.kwargs['cat_slug'], availability=True).count()
        context['subcategory_list'] = SubCategory.objects.filter(cat__url=self.kwargs['cat_slug'])
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class SubCategoryYarnList(DataMixin, ListView):
    paginate_by = 16
    template_name = 'shop/subcategory_yarn_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        form = YarnOrderingForm(self.request.GET)
        yarn = Yarn.objects.filter(subcat__url=self.kwargs['subcat_slug'], availability=True).order_by('name').select_related('subcat')
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Yarn.objects.filter(subcat__url=self.kwargs['subcat_slug']).count()
        context['subcategory_object'] = SubCategory.objects.get(url=self.kwargs['subcat_slug'])
        c_def = self.get_user_context()
        context = (dict(list(context.items()) + list(c_def.items())))
        return context


class FilterYarnList(DataMixin, ListView,):
    paginate_by = 16
    template_name = 'shop/search-filter_yarn_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        q = Q()
        if "country" in self.request.GET:
            q = Q(subcat__count__in=self.request.GET.getlist("country"))
        if "producer" in self.request.GET:
            q &= Q(subcat__prod__in=self.request.GET.getlist("producer"))
        if "color" in self.request.GET:
            q &= Q(col__in=self.request.GET.getlist("color"))
        if "max-price" in self.request.GET:
            q &= Q(subcat__price__lte=self.request.GET['max-price'])
        if "available" in self.request.GET:
            q &= Q(availability=self.request.GET['available'])

        form = YarnOrderingForm(self.request.GET)
        yarn = Yarn.objects.filter(q).distinct().select_related('subcat')
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):
        availability = f'available={self.request.GET.get("available")}&'
        if "available" not in self.request.GET:
            availability = ''

        context = super().get_context_data(**kwargs)
        context['price'] = f'max-price={self.request.GET["max-price"]}&'
        context['producer'] = ''.join([f'producer={x}&' for x in self.request.GET.getlist("producer")])
        context['country'] = ''.join([f'country={x}&' for x in self.request.GET.getlist("country")])
        context['color'] = ''.join([f'color={x}&' for x in self.request.GET.getlist("color")])
        context['available'] = availability
        context['count'] = Yarn.objects.filter(availability=True).count()
        c_def = self.get_user_context()
        context = (dict(list(context.items()) + list(c_def.items())))
        return context


class SearchYarnList(DataMixin, ListView):
    paginate_by = 16
    template_name = 'shop/search-filter_yarn_list.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        form = YarnOrderingForm(self.request.GET)
        yarn = Yarn.objects.filter(name__icontains=self.request.GET.get('query')).order_by('name').select_related('subcat')
        if form.is_valid():
            if form.cleaned_data["ordering"]:
                return yarn.order_by(form.cleaned_data["ordering"])
        return yarn.order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = Yarn.objects.filter(availability=True).count()
        context['q'] = f'query={self.request.GET.get("query")}&'
        c_def = self.get_user_context()
        context = (dict(list(context.items()) + list(c_def.items())))
        return context


class YarnDetail(DetailView):
    model = Yarn
    template_name = 'shop/yarn_detail.html'

    def get_object(self, queryset=None):
        return Yarn.objects.get(url=self.kwargs['product_slug'])

    def get_context_data(self, *args, **kwargs):
        cart_yarn_form = CartAddYarnForm()
        context = super().get_context_data(**kwargs)
        context['cart_yarn_form'] = cart_yarn_form
        context['yarns'] = Yarn.objects.all()
        return context





