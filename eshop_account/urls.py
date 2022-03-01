from django.urls import path
from .views import login_user, register


app_name = 'eshop_account'
urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register, name='register'),
]