

'''
#views d' crm

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect

# from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PersonForm0, PersonForm1, PersonForm2, PersonForm, ContactForm, PersonPhotoForm
from .models import Person, Photo

'''

from django.shortcuts import render, redirect

def printing(request):
    template_name = '/dashboard/'
    print('ativido o ----------------------modulo')
    return redirect(template_name)
'''
def person_as_p(request):
    template_name = 'crm/person_form_as_p.html'
    #form = PersonForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/crm/person_list/')

    context = {'form': form}

    return render(request, template_name, context)
'''