from django import template
from shop.models import *

register = template.Library()


@register.inclusion_tag('shop/tags/recently_added.html')
def recently_added():
    yarn = Yarn.objects.order_by("-id")[:4]
    return {'yarn': yarn}


@register.simple_tag()
def get_categories():
    return Category.objects.all()