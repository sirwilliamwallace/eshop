from django import forms
from django.core import validators


class ContactMe(forms.Form):
    name = forms.CharField(
        label='نام و نام خانوادگی',
        label_suffix='',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "نام و نام خانوادگی"}),
        validators=[validators.MaxLengthValidator(150, "نام و نام خانوادگی باید کمتر از 150 کاراکتر باشد")]
    )
    email = forms.EmailField(
        label='ایمیل',
        label_suffix='',
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', "placeholder": "ایمیل"}),
        validators=[validators.MaxLengthValidator(100, "ایمیل باید کمتر از 100 کاراکتر باشد")]
    )
    subject = forms.CharField(
        label='موضوع',
        label_suffix='',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "موضوع"}),
        validators=[validators.MaxLengthValidator(150, "موضوع باید کمتر از 150 کاراکتر باشد")]
    )
    message = forms.CharField(
        label='پیام',
        label_suffix='',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', "placeholder": "پیام", "rows": "8", "id": "message"}, ),
    )
