from django.urls import path

from .views import *

urlpatterns = [
    path('category/<slug:slug>/', yarncategory, name='category'),
    path('', main, name='main')
]