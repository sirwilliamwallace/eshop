from django import forms


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
