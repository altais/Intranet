#-*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from contact.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact