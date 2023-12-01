from django.urls import path

from .views import *

urlpatterns = [
    path('search/', Search.as_view(), name='search'),
    path('', ProductList.as_view(), name='main'),
    path('category/<slug:cat_slug>/', CategoryProductList.as_view(), name='category'),
    path('subcategory/<slug:subcat_slug>/', SubCategoryProductList.as_view(), name='subcat'),
    path('filter/', FilterYarnList.as_view(), name='filter'),
    path('<slug:product_slug>/', ProductDetail.as_view(), name='product_detail'),
]