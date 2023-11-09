from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from shop.models import Yarn


def main(request):
    yarn = Yarn.objects.filter(availability=True)
    return render(request, 'shop/main.html', {'yarn': yarn})


def yarncategory(request):
    return HttpResponse('hello')