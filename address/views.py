from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic import CreateView

#views d' crm

from django.views.generic import CreateView
from .forms import MyCep_Form,StateForm
from .models import Cep,VinCep





def printing(request):
    template_name = '/dashboard/'
    print('ativido o ----------------------modulo')
    return redirect(template_name)


def address_list(request):
    template_name = 'suppliers/suppliers_list.html'
    object_list = VinCep.objects.all()
    form=StateForm#form do ajax
    context = {'object_list': object_list,'form':form}
    return render(request, template_name, context)



#basedo em buscar por cep
#apresentação do form
def address_as_p(request):
    
    print('view address- address_as_P flou 29')
    
    template_name = 'address/address_form_as_p.html'
    form = MyCep_Form
   


    if request.method == 'POST':
        if form.is_valid():
            print('view address- address_as_P flou 38')
            form.save()
            return redirect('/crm/person_list/')

     

    context = {'form': form, }
    print(context)
    return render(request, template_name, context)




def filter_cep(request):
     template_name = 'address/filter_cep.html'
     print('view address- filter_cep flou 53')
     context={}
     try:
            cep=" "
            bairro="-?-"
            cidade="-?-"
            endereco="-?-"
            uf="-*"
            print('view address- filter_cep flou 61')
         
            context['cep']=cep
            context['cidade']=cidade
            context['bairro']=bairro
            context['endereco']=endereco
            context['uf']=uf
              
     except ObjectDoesNotExist:

            bairro='não localizado'
            cidade='não localizado'
            endereco='não localizado'
            uf='x'
            print('view address- filter_cep flou 75')
   
            context['cep']=cep
            context['cidade']=cidade
            context['bairro']=bairro
            context['endereco']=endereco
            context['uf']=uf

     if request.method == 'GET':
      print('view address- filter_cep flou 84')
      cep= request.GET.get('cep')
        
     try:
        consulta=Cep.objects.get(cep=cep)
        print('view address- filter_cep flou 89')
        bairro=consulta.bairro
        cidade=consulta.cidade
        endereco=consulta.endereco
        uf=consulta.uf
        print('view address- filter_cep flou 94')
       
        context['cep']=cep
        context['cidade']=cidade
        context['bairro']=bairro
        context['endereco']=endereco
        context['uf']=uf
        data=[endereco,bairro,cidade,uf]
        print('view address- filter_cep flou 102 JsonResponse data')
        return JsonResponse({'data': data})

          
     except ObjectDoesNotExist:
        bairro='não existe'
        cidade='não existe'
        endereco='não localizado'
        uf='--'
        print('view address- filter_cep flou 108')
       
        context['cep']=cep
        context['cidade']=cidade
        context['bairro']=bairro
        context['endereco']=endereco
        context['uf']=uf

           
        print('view address- filter_cep flou 117')
     
     return render(request,template_name,context)

def ceps_ajax(request):
    print('view address- ceps_ajax flou 122')
    template_name = 'address/address_form_as_p.html'
    context={}

   

    if request.method == 'GET':
      print('view address- ceps_ajax flou 129')
      cep= request.GET.get('cep')
        
    try:
        consulta=Cep.objects.get(cep=cep)
        bairro=consulta.bairro
        cidade=consulta.cidade
        print('view address- ceps_ajax flou 136')
       
        context['cep']=cep
        context['cidade']=cidade
        context['bairro']=bairro
          
    except ObjectDoesNotExist:
        bairro='não existe'
        cidade='não existe'
        print('view address- ceps_ajax flou 145')
       
        context['cep']=cep
        context['cidade']=cidade
        context['bairro']=bairro

           
        print('view address- ceps_ajax flou 152')
   
       
    return render(request,template_name,context)

