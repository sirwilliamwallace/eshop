from django.shortcuts import render


def header(request, *args, **kwargs):
    context = {
        "title": "It's a Eshops"
    }
    return render(request, 'shared/Header.html', context)


def footer(request, *args, **kwargs):
    context = {
        "about_us": "I'm nUmberX",
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):
    context = {
        'data': 'Hello World'
    }
    return render(request, 'home_page.html', context)
