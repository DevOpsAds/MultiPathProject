from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from chartjs.views.lines import BaseLineChartView

from datetime import datetime

from .forms import SupplierAll,SupplierList
from .models import meterorologia,Supplier
#from .filters import 
#ia Kanask
from .controller import infor_meteorologia,memory_binary,met_decea_mil       #neuro_training,math_mathematical

#from address.models import Cep
from app.models import Active,TimeStampedModel

import json
#print('line:23,def: start as atividade iA '+ str(math_mathematical()))

infor_meteorologia('inf')

# 09/08/2023 _JB4.
# 08/09/2023 _JB4.

class iA_ZanasK(View):

    def get(self,request):
        
        template_name ='supplier/grafico.html'
        data={
        "labels":["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho"],
        "datesets":[
                { 
                    "label":"Vendas",
                    "backgroundColor":"rgba(75,192,192,0.2)",
                    "borderColor":"rgba(75,192,191,1)",
                    "data":[100,150,200,120,180],
                }
    
            ],
        }
        return render(request,template_name,{"data":data})


class SuppliersCreateView(View):


    def get(self,request):
        closeModal=request.GET.get('closeModal')
        #print('line:28,def: GET MODAL CLOSE,form page: views,evento_investigado: atividade controller '+ str(closeModal))
        template_name ='supplier/supplier_as_p.html'
        form = SupplierAll(request.POST or None)
        context={'form':form,'modalVisible':closeModal }
        return render(request,template_name,context) 

    def post(self,request):
        template_name ='supplier/supplier_list.html'
        form = SupplierAll(request.POST or None)
        if request.method == 'POST':

            if form.is_valid():
                print(request.POST)
                form.save()
                return redirect('supplier:SuppliersListView') 

        context={'form':form}      
        return render(request,template_name) 

class Number:
    def __int__(self,value):
        self.value=value
    def list_numeros():
        numeros=[1,2,3]
        objetos_numeros=[Number(numero)for numero in numeros] 

    def __str__(self):
       return str(self.objetos_numeros)


class SuppliersListView(View):


    def get(self,request):
        #meteorologia('dk')
        #print('line:23,def: retifica _list,form page: supplier_list,evento_investigado: atividade controller '+ str(starting()))
        template_name ='supplier/supplier_list.html'
        form = SupplierList(request.POST or None)
         
        object_list = Supplier.objects.all()  
        days_modified=[]


        for e in object_list.filter():
            print (e.modified)
            data_system=e.modified
            days_modified.append({'ultimas_modificacoes':cauculate_time_difference(data_system,'-')})


            #(entrada,desejado,obtito,weight):
      
 

        obj_numeros = Number
        #data_modified=object_list.trade_name
        numero={
        'nome':"este",
        'descripion':'casa'
        },{
        'nome':"zeca",
        'descripion':'fora'
        },{
        'nome':"tercerio",
        'descripion':'fora'
        }
    
        

        bola={}

        ultimas_modificacoes=days_modified

        combinate=zip(object_list,ultimas_modificacoes)


        for b in bola:
            print(b)

        context = {'object_list': object_list,'form':form,'bola':combinate}
        

        return render(request,template_name,context) 

    def post(self,request):
        template_name ='supplier/supplier_list.html'
        form = SupplierAll(request.POST or None)
        if request.method == 'POST':

            if form.is_valid():
                print(request.POST)
                #form.save()
                context={'form':form}
                return render(request,template_name,context) 

        context={'form':form}      
        return render(request,template_name)   


class SuppliersDetailView(View):

    def get(self,request,pk):
        #print('line:23,def: retifica _list,form page: supplier_list,evento_investigado: atividade controller '+ str(starting()))
        template_name ='supplier/supplier_detail.html'
        #form = SupplierList(request.POST or None)
        obj = Supplier.objects.get(pk=pk)
        context = {'object': obj}
        print('line:80,def: SuppliersDetailView ,form page: views,evento_investigado: capurar nome lista suppliers_detail'+ str(obj))        
        #context = {'object_list': object_list,'form':form}
        return render(request,template_name,context) 

    def post(self,request):
        template_name ='supplier/supplier_detail.html'
        form = SupplierAll(request.POST or None)
        if request.method == 'POST':

            if form.is_valid():
                print(request.POST)
                #form.save()
                context={'form':form}
                return render(request,template_name,context) 

        context={'form':form}      
        return render(request,template_name)   


class SuppliersUpdateView(View):
    

    #print('line:103,def: Update _list,form page: supplier_list,evento_investigado: #1- integração corrente do codigo'+ str(starting()))

    def get(self,request,pk):
        template_name ='supplier/supplier_as_p.html'
        instance = Supplier.objects.get(pk=pk)
        form = SupplierAll(request.POST or None, instance=instance)
  
        print('nova linha')
        print(pk)
     
    
        context={'form':form}      
        return render(request,template_name,context)   

    def post(self,request,pk):

     if request.method == 'POST':
            template_name ='supplier/supplier_as_p.html'
            instance = Supplier.objects.get(pk=pk)
            form = SupplierAll(request.POST or None, instance=instance)

            if form.is_valid():
                supplier= form.save()
                return redirect('supplier:SuppliersDetailView', supplier.pk)

class SuppliersDeleteView(View):
    

    def get(self,request,pk):
        template_name ='supplier/supplier_detail.html'
        obj = Supplier.objects.get(pk=pk)
        btn_visivel="True"
        msg="Ao clicar em delete esse cadastro será completamente eliminado do sistema!"
        classAlert="alert alert-danger"

        context = {'object': obj,'msg':msg ,'class':classAlert,'delete':btn_visivel}

    
        return render(request,template_name,context)   







#leitura de dados para carregar a inteligencia artificial
def documents_ia_Kanask(request):
    template_name ='supplier/supplier_detail.html'
    
    json_path='arquivo_Artificial1.json'
    
    with open(json_path,'r') as json_file:
        dados=json.load(json_file)
   
    return JsonResponse({'dados': dados})

 
      



                
            

def suppliers_list():
    ...   

def suppliers_create():
    ...

def suppliers_detail():
    ...

def suppliers_update():
    ... 
@csrf_exempt
def supplier_delete(request,pk):
    print('line:166,def: suppliers_delete,form page: views,evento_investigado: event delete ok'+ str(pk))
    supplier =get_object_or_404(Supplier,pk=pk)
    supplier.delete()
    return redirect('supplier:SuppliersListView')


def cep_zanask(request):
    #http://localhost:8000/address/filter_cep/?cep=30880-420
    cep=request.POST.get('cep')
    consulta=Cep.objects.get(cep=cep)
    print('line:175,def: cep facila cep_zanask,form page: def_zanask,evento_investigado: #2'+ str(consulta))
    return(consulta)
 
def cauculate_time_difference(date_system,attri):
    data_atual=timezone.localtime(timezone.now())
    modified_time=datetime.strftime(date_system,"%Y-%m-%d %H:%M:%S")
    now_time=datetime.strftime(data_atual,"%Y-%m-%d %H:%M:%S")
    #print("data_modificada",modified_time)
    if attri=='+':
        current_datetime=data_atual+date_system
        #print(' somar hora atual e data:',str(current_datetime))

    if attri=='-':
        current_datetime=data_atual-date_system
        current_datetime=current_datetime.days
        #print(' line:250:> subtrair hora atual e data:',current_datetime)
        return current_datetime

def meteorologia(inf):    
    print(met_decea_mil())
    data = {}
    objects = meterorologia.objects.all()
    data=[met_decea_mil()]
    #objects.save()