from django import forms
from django.core import validators
from django.contrib.auth.models import User


class OrderForm(forms.Form):
    productId = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
    tedad = forms.IntegerField(
        label='تعداد',
        widget=forms.NumberInput(),
        initial=1,
    )
