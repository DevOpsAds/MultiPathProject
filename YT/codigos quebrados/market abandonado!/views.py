

'''
#views market' crm

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect

# from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PersonForm0, PersonForm1, PersonForm2, PersonForm, ContactForm, PersonPhotoForm
from .models import Person, Photo

'''
#from .forms import LogMarket_Form
from django import forms
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime
#from .models import LogMarket
from django.shortcuts import render, redirect

class Dtform(forms.Form):
    datetime=forms.DateTimeField(widget=AdminSplitDateTime())

def printing(request):
    template_name = '/dashboard/'
    print('ativido o ----------------------modulo')
    return redirect(template_name)

def market_as_p(request):
    template_name = 'market/market_form_as_p.html'
   # form = LogMarket_Form(request.POST or None)

    if request.method == 'POST':
       if form.is_valid():
          form.save()
          context = {'form': form}

          return render(request, template_name,context)

    context = {'form': form}


    return render(request, template_name, context)