from django.shortcuts import render

from site_settings.models import SiteSetting
from .models import Contact
from .forms import ContactMe


# Create your views here.
def contact_us(request):
    form = ContactMe(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        form = ContactMe()
    setting = SiteSetting.objects.first()
    context = {
        "form": form,
        "setting": setting,
    }
    return render(request, 'contact_us/contact_us.html', context)
