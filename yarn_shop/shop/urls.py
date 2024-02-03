from django.urls import path

from .views import *

urlpatterns = [
    path('search/', SearchProductList.as_view(), name='search'),
    path('filter/', FilterProductList.as_view(), name='filter'),
    path('', ProductList.as_view(), name='main'),
    path('category/<slug:cat_slug>/', CategoryProductList.as_view(), name='category'),
    path('subcategory/<slug:subcat_slug>/', SubCategoryProductList.as_view(), name='subcategory'),
    path('<slug:product_slug>/', ProductDetail.as_view(), name='product_detail'),
]