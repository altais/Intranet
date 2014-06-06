#-*- coding: utf-8 -*-
from contact.models import *
from contact.forms import *
from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(form.cleaned_data['sujet'], form.cleaned_data['message'], form.cleaned_data['email'], ['cervantescedric@gmail.com'])
            send = True
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', locals())