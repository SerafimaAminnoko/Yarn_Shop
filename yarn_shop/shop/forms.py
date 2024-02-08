from django import forms

from shop.models import Yarn


class YarnOrderingForm(forms.Form):
    ordering = forms.ChoiceField(label='Order_by', required=False,  choices=[
        ['name', 'by_alphabet'],
        ['subcat__price', 'cheap_on_top'],
        ['-subcat__price', 'expensive_on_top']
    ])




