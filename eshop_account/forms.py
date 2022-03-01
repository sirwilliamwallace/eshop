from django import forms
from django.core import validators
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    user_name = forms.CharField(
        label='نام کاربری ',
        label_suffix='',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}),
        required=True,
    )
    password = forms.CharField(
        label='رمز عبور ',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}),
        required=True,
    )


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        label='نام کاربری ',
        label_suffix='',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}),
        required=True,
        validators=[
            validators.MaxLengthValidator(100, 'نام کاربری باید کمتر از 100 کاراکتر باشد'),
            validators.MinLengthValidator(3, 'نام کاربری باید حداقل 3 کاراکتر باشد'),
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}),
        required=True,
        validators=[
            validators.EmailValidator(message='ایمیل وارد شده معتبر نمی باشد'),
        ]
    )
    password = forms.CharField(
        label='رمز عبور ',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد کنید'}),
        required=True,
        validators=[
            validators.MinLengthValidator(8, 'رمز عبور باید حداقل 8 کاراکتر باشد'),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور ',
        label_suffix='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور خود را وارد کنید'}),
        required=True,
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('رمز عبور و تکرار آن باید یکسان باشند')
        return confirm_password

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        qs = User.objects.filter(username=user_name)
        if user_name.isdigit():
            raise forms.ValidationError('نام کاربری نمی تواند تنها از عدد تشکیل شده باشد')
        elif qs.exists():
            raise forms.ValidationError('نام کاربری قبلا گرفته شده است')
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('ایمیل قبلا گرفته شده است')
        return email


