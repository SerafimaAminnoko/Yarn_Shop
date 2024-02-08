from django.urls import path

from .views import *

urlpatterns = [
    path('search/', SearchYarnList.as_view(), name='search'),
    path('filter/', FilterYarnList.as_view(), name='filter'),
    path('', YarnList.as_view(), name='main'),
    path('category/<slug:cat_slug>/', CategoryYarnList.as_view(), name='category'),
    path('subcategory/<slug:subcat_slug>/', SubCategoryYarnList.as_view(), name='subcategory'),
    path('<slug:product_slug>/', YarnDetail.as_view(), name='product_detail'),
]