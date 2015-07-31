from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import SignUpForm, ContactForm
# Create your views here.
def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
    context = {
        'form': form,
        'result': 'Prepate your message!'
    }
    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    result = ''
    if form.is_valid():
        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        messsage = form.cleaned_data.get('messsage')
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, from_email]
        contact_message = '%s: %s via %s'%(full_name, messsage, email)
        try:
            send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
            result = 'Bottle sended!'
        except:
            result = 'The crow was shoted. Try Again.'
    context = {
        'form': form,
        'result': result,
    }
    return render(request, 'forms.html', context)
