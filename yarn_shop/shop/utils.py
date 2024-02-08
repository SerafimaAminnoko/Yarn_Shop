from django.db.models import Min, Max, Avg
from shop.forms import YarnOrderingForm
from shop.models import *


class Filters:
    def get_minMaxPrice(self):
        return SubCategory.objects.aggregate(Min('price'), Max('price'), Avg('price'))

    def get_colors(self):
        return Color.objects.all()

    def get_producers(self):
        return Producer.objects.all()

    def get_countries(self):
        return Country.objects.all()


class DataMixin(Filters):
    def get_user_context(self, **kwargs):
        context = kwargs
        context['minMaxPrice'] = Filters.get_minMaxPrice(self)
        context['form'] = YarnOrderingForm(self.request.GET)
        context['ordering'] = f'ordering={self.request.GET.get("ordering") or "name"}&'
        context['paginate_by'] = f"paginate_by={self.request.GET.get('paginate_by', self.paginate_by)}&"
        return context