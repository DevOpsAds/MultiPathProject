#views d' crm
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect

# from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PersonForm0, PersonForm1, PersonForm2, PersonForm, ContactForm, PersonPhotoForm
from .models import Person, Photo


def person_list(request):
    template_name = 'crm/person_list.html'
    object_list = Person.objects.all()
    form=PersonForm2#form do ajax
    context = {'object_list': object_list,'form':form}
    return render(request, template_name, context)


def person_detail(request, pk):
    template_name = 'crm/person_detail.html'
    obj = Person.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def person_create(request):
    template_name = 'crm/person_form0.html'
    form = PersonForm0(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/crm/person_list/')

    context = {'form': form}

    return render(request, template_name, context)


def person_create1(request):
    template_name = 'crm/person_form1.html'
    form = PersonForm1(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/crm/person_list/')

    context = {'form': form}

    return render(request, template_name, context)


def person_create2(request):
    template_name = 'crm/person_form2.html'
    form = PersonForm2(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/crm/person_list/')

    context = {'form': form}

    return render(request, template_name, context)


def person_as_p(request):
    template_name = 'crm/person_form_as_p.html'
    form = PersonForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/crm/person_list/')

    context = {'form': form}

    return render(request, template_name, context)


def person_detaill(request, pk):
    template_name = 'crm/person_detail.html'
    obj = Person.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def person_update(request, pk):
    template_name = 'crm/person_form_as_p.html'
    instance = Person.objects.get(pk=pk)
    form = PersonForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/crm/person_list/')

    context = {'form': form}
    return render(request, template_name, context)

#docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog


def send_contact(request):
    template_name = 'crm/contact_form.html'
    form = ContactForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            print('contato_*****>valid')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            sender = form.cleaned_data.get('sender')
            send_mail(
                subject,
                message,
                sender,
                ['localhost'],
                fail_silently=False,
            )

            return redirect('/dashboard/')
    context = {'form':form}
    return render(request, template_name, context)

class PersonBootstrapCreate(CreateView):
    model=Person
    form_class=PersonForm
    template_name= 'crm/person_bootstrap_form.html'


class PersonCrispyCreate(CreateView):
    model=Person
    form_class=PersonForm
    template_name= 'crm/person_crispy_form.html'

def photo_create(request):
    data = {}
    template_name = 'crm/person_photo_form.html'
    form = PersonPhotoForm(request.POST or None)
    if request.method == 'POST':
           photo = request.FILES.get('photo')
           if form.is_valid():
               person= form.save()
               Photo.objects.create(person=person, photo=photo)
               data['msg'] = str('Foto anexada com sucesso!')
               data['class'] = 'alert-success'
               return redirect('crm:person_detail', person.pk)


    context={'form':form}
    return render(request, template_name, context)

def person_create_ajax(request):
    #template_name = 'o templete no caso esta em list onde será incoporado o form '
    form= PersonForm2(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            person=form.save()
            data=[person.to_dict()]

            return JsonResponse({'data': data})

def person_vuejs_list(request):
    template_name= 'crm/person_vuejs_list.html'
    return render(request,template_name)

def person_json(request):
    # Retorna os dados
    persons = Person.objects.all()
    data = [person.to_dict() for person in persons]
    return JsonResponse({'data': data})

def person_vuejs_create(request):
    #template_name = 'o templete no caso esta em list onde será incoporado o form '
    form= PersonForm2(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            person=form.save()
            data=person.to_dict()

            return JsonResponse({'data': data})

def person_vuejs_update(request, pk):
    person = Person.objects.get(pk=pk)
    form = PersonForm2(request.POST or None, instance=person)

    if request.method == 'POST':
        if form.is_valid():
            person = form.save()
            data = person.to_dict()
            return JsonResponse({'data': data})


def person_vuejs_delete(request, pk):
    if request.method == 'DELETE':
        person = Person.objects.get(pk=pk)
        person.delete()
    return JsonResponse({'status': 204})