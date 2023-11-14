from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:cat_slug>/', CategoryProductList.as_view(), name='category'),
    path('', ProductList.as_view(), name='main'),
]