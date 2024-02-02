from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import LogChip_Form,StateForm,myAdress_Form
from django import forms
from django.http import JsonResponse
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime

from .models import Mineralandia,Cliente,Telefone,City,District,Persona
from crm.views import person_list



def person_list(request):
    template_name = 'crm/person_list.html'
    object_list = Person.objects.all()
    form=StateForm#form do ajax
    context = {'object_list': object_list,'form':form}
    return render(request, template_name, context)



class Dtform(forms.Form):
    datetime=forms.DateTimeField(widget=AdminSplitDateTime())
# Create your views here.

def printing(request):
    template_name = '/dashboard/'
    print('ativido o ----------------------modulo')
    return redirect(template_name)

def chip_as_p(request):
    template_name = 'relacionChip/relacionChip_form_as_p.html'
    form = LogChip_Form(request.POST or None)
    mineralandia=Mineralandia.objects.create(code="1221", cliente=0, telefone="3787183")


    if request.method == 'POST':
       if form.is_valid():
          form.save()
          context = {'form': form}
          print('accesso 1')

          return render(request, template_name,context)

    context = {'form': form}

    print(mineralandia )
    return render(request, template_name, context)

   
def create_insert_in_cliente(request):
	#criar insert de dados em mutiplas tabelas
  
    cliente=Cliente.objects.create(nome="12245")
    telefone=Telefone.objects.create(numero="111242",cliente=cliente)
    telefone=Telefone.objects.create(numero="2222452",cliente=cliente)
    
'''
def manual_m(request):

	template_name = 'relacionChip/relacionChip_form_as_p.html'
	clientes=Cliente.objects.all().values('id','nome')
	form = LogChip_Form(request.POST or None)
	cliente=Telefone.objects.filter(numero="111242")

	print(form)

   

def kipmanual_m(request):

	template_name = 'relacionChip/relacionChip_form_as_p.html'
	clientes=Cliente.objects.all().values('id','nome')
	form = LogChip_Form(request.POST or None)
	cliente=Telefone.objects.filter(numero="111242")

    if request.method == 'POST':
    	if form.is_valid():
        form.save()
        context = {'form': form}
        print('accesso 1')

        return render(request, template_name,context)

    context = {'form': form}
 

	print(form)
	return render(request, template_name,context)
'''
def visto_manual_m(request, *callback_args, **callback_kwargs):
    template_name = 'relacionChip/relacionChip_form_as_p.html'

    fornecedor=Cliente.objects.filter(nome='12245s')
    print(fornecedor)
   
    form = LogChip_Form(request.POST or None)
    form.fields['telefone'].choices=[(fornecedor,fornecedor)for fornecedor in fornecedor]
    #[(id,fornecedor)for id,fornecedor in fornecedor]
    if request.method == 'POST':
       if form.is_valid():
          form.save()
          context = {'form': form}

          return render(request, template_name,context)

    context = {'form': form}
    print(fornecedor)


    return render(request, template_name, context)


def manual_m(request, *callback_args, **callback_kwargs):
    form = LogChip_Form(request.POST or None)

    template_name = 'relacionChip/relacionChip_form_as_p.html'

    if request.method == 'GET':

     id_cliente=request.GET


     if id_cliente:
      id_filter=id_cliente['idSelect']

      #metodo correto retorna none.
      telefone_id=request.POST.get('data')
      
      print(telefone_id)

      number=Telefone.objects.filter(cliente=id_filter)
      
      cliente=Cliente.objects.all()
      print(number)

      form.fields['cliente'].choices=[(cliente,cliente)for cliente in cliente]

      form.fields['telefone'].choices=[(number,number)for number in number]

      context = {'form': form}
      return redirect('http://localhost:8000/chip/manual/?idSelect=25')

 
      

    
    #ver detatlhe de embalage,m
    numbersemEmbalagem=Telefone.objects.get(cliente=25)
    
   
 
   
    #[(id,fornecedor)for id,fornecedor in fornecedor]
    if request.method == 'POST':
       if form.is_valid():
          form.save()
          context = {'form': form}

          return render(request, template_name,context)

    context = {'form': form}
    #print(form)
    return render(request, template_name,context)


    



def pd_redirect(request):
        form = LogChip_Form(request.POST or None)

        print(form)
        return HttpResponse(form)

#filtro list dang#1 material complementar abordo.

def filter_list(request):
     template_name = 'relacionChip/filter_list.html'
     context={}
     cities=City.objects.all()
     district=District.objects.all()
     muniple=(
        ('MG','Minas Gerais'),
        ('ES','Espirito Santo'),
        ('SP','São Paulo'),
        ('RJ','Rio de Janeiro'),
        ('PR','Paraná'),)
   
     context['states']=muniple
     context['cities']=cities
     context['districts']=district
    
     return render(request,template_name,context)

def cities_ajax(request):
    uf= request.GET.get('uf')
    cities=City.objects.filter(uf=uf)
    context={'cities':cities}
    return  render(request,'includes/components/_cities.html',context)

def districts_ajax(request):
    city= request.GET.get('city')
    districts=District.objects.filter(city=city)
    context={'districts':districts}
    return  render(request,'includes/components/_districts.html',context)

#dropdown filtros encadeads
def filter_dropdown(request):
    context={}
    context['form']=StateForm(state)
    q=request.GET.get('district')

    if q:
        q = q.replace('.','')
        persons=Persona.objects.filter(district=str(q))
        context['persons']=persons
    return  render(request,'relacionChip/filter_dropdown.html',context)



def city_choices_ajax(request):
    #print("acessp a city_choices_ajax")
    uf=request.GET.get('uf')
    cities=City.objects.filter(uf=uf)
    context={'cities':cities}
    return render(request,'includes/components/_city_choices_ajax.html',context)

def districts_choices_ajax(request):
       #print("acessp a city_choices_ajax")
    city=request.GET.get('city')
    districts=District.objects.filter(city=city)
    context={'districts':districts}
    return render(request,'includes/components/_districts_choices_ajax.html',context)





def filter_dropdown2(request):
    context = {}
    state = request.GET.get('state')
    print(state)
    city =  request.GET.get('city')

    print(city)
    context['form']=StateForm(state,city)
    q = request.GET.get('district')
    print(q)
   
    # Filtro
    q = request.GET.get('district')
    if q:
         q = q.replace('.', '')
         persons = Persona.objects.filter(district=str(q))
         context['persons'] = persons
    
       

    return render(request, 'relacionChip/filter_dropdown2.html', context)
