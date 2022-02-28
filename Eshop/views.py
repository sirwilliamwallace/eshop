from django.shortcuts import render


def home_page(request):
    context = {
        'data': 'Hello World'
    }
    return render(request, 'home_page.html', context)