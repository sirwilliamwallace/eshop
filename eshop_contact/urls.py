from django.urls import path
from .views import contact_us


app_name = 'eshop_contact'
urlpatterns = [
    path('/contact-us', contact_us, name='contact'),
]