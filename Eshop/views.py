from django.shortcuts import render
from eshop_sliders.models import Slider
from site_settings.models import SiteSetting


def header(request, *args, **kwargs):
    setting = SiteSetting.objects.first()
    context = {
            "setting": setting,
    }
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    setting = SiteSetting.objects.first()
    context = {
        "setting": setting,
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'sliders': sliders,
    }
    return render(request, 'home_page.html', context)
def about_us (request):
    setting = SiteSetting.objects.first()
    context = {
        "setting": setting,
    }
    return render(request, 'about-us.html', context)
