from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='main'),
    path('category/<slug:cat_slug>/', CategoryProductList.as_view(), name='category'),
    path('subcategory/<slug:subcat_slug>/', SubCategoryProductList.as_view(), name='subcat'),
    path('filter/', FilterYarnList.as_view(), name='filter')
]