from django.shortcuts import render
from eshop_sliders.models import Slider

def header(request, *args, **kwargs):
    context = {
        "title": "nUmberX",
    }
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    context = {
        "about_us": "I'm nUmberX",
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'sliders': sliders,
    }
    return render(request, 'home_page.html', context)
