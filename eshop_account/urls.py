from django.urls import path
from .views import login_user,logout_user, register_user # autherize_user


app_name = 'eshop_account'
urlpatterns = [
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_user, name='register'),
]