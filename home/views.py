from django.shortcuts import render

from django.contrib import messages
from django.conf import settings

from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactUsForm


# Create your views here.
def index(request):
    """ Renders the home template """
    return render(request, 'home/index.html')


def about_us(request):
    """presents the about us page"""
    template_name = 'home/connect.html'
    return render(request, template_name)


def contact_us(request):
    """Renders the contact us page"""
    phone = settings.DEFAULT_FROM_PHONE
    cmp_email = settings.DEFAULT_FROM_EMAIL
    address = settings.DEFAULT_FROM_ADDRESS

    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES)
        if form.is_valid():
            sender = request.POST['name']
            from_email = request.POST['email']
            form_message = request.POST['body']
            subject = render_to_string(
                'home/contact_us_email/contact_us_email_subject.txt',
                {'sender': sender})
            message = render_to_string(
                'home/contact_us_email/contact_us_email_body.txt',
                {
                    'sender': sender,
                    'form_message': form_message,
                    'from_email': from_email
                    })
            send_mail(
                subject,
                message,
                from_email,
                [cmp_email],
                )
            messages.success(request, 'Message Sent!')
            return render(request, 'home/connect.html', {'message_sent': True})
    else:
        form = ContactUsForm()
    context = {
        'phone': phone,
        'cmp_email': cmp_email,
        'address': address,
        'form': form,
        'contact_us': True
    }
    template_name = 'home/connect.html'
    return render(request, template_name, context)


def privacy_policy(request):
    """Renders the privacy policy page"""
    template_name = 'home/privacy_policy.html'
    return render(request, template_name)
