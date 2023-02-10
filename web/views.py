from django.shortcuts import render, redirect
from . forms import *
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.

def index(request):
    if (request.method == 'POST'):
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        sender=request.POST.get('email')
        recipient=['halisidjangomails@gmail.com']
        contact_form=Contact(request.POST)
        if contact_form.is_valid():
            send_mail(
                subject,
                'From '+ name + message,
                sender,
                recipient,
            )
            contact_form.save()
            return HttpResponse('Thank you! We will get back to you soon!')
        else:
            return redirect('web:index')
    else:
        contact_form=Contact()
    return render(request, 'web/index.html',{'contact_form':contact_form})