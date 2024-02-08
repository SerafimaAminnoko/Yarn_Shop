from django import forms

YRN_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddYarnForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=YRN_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
