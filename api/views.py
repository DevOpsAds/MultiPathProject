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

from .forms import ApiQualificPensonAll,ApiGrandezaPerson
from .models import CallApiQualification_grandezas_Person,CallApiQualificationGrandezas
#from .filters import 
#ia Kanask
#from .controller import memory_binary       #neuro_training,math_mathematical

#from address.models import Cep
from app.models import Active,TimeStampedModel

import json

#29/08/2023 - coding at iA zanask
#10/09/2023 -cronometro
#memory_binary()
# _JB4.

# rota painel entrada de dados de login
def cronometro_protocolos(request):
    return render (request,'painel.html')


class ApiCronomentView(View):

	def get(self,request):


		#closeModal=request.GET.get('closeModal')
		#print('line:28,def: GET MODAL CLOSE,form page: views,evento_investigado: atividade controller '+ str(closeModal))
		template_name ='api/cronometro.html'
		#form = ApiQualificPensonAll(request.POST or None)
        
		#context={'form':form,'modalVisible':closeModal, }
		return render(request,'cronometro.html')

	def post(self,request):
		template_name ='api/api_list.html'
		 #form = SupplierAll(request.POST or None)
		if request.method == 'POST':

				print(request.POST)
				return redirect('api/api_as_p.html') 

		context={'form':form}      
		return render(request,template_name) 

class iA_ZanasK(View):

    def get(self,request):
        
        template_name ='api/grafico.html'
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
class ApiCreateView(View):

	def get(self,request):


		closeModal=request.GET.get('closeModal')
		#print('line:28,def: GET MODAL CLOSE,form page: views,evento_investigado: atividade controller '+ str(closeModal))
		template_name ='api/api_as_p.html'
		form = ApiQualificPensonAll(request.POST or None)
        
		context={'form':form,'modalVisible':closeModal, }
		return render(request,template_name,context) 

	def post(self,request):
		template_name ='api/api_list.html'
		 #form = SupplierAll(request.POST or None)
		if request.method == 'POST':

				print(request.POST)
				return redirect('api/api_as_p.html') 

		context={'form':form}      
		return render(request,template_name) 

def set_cookie_view(request):
	#codigo fucionado salvo em django cookes  navegado explore  python tutorial net

		visited=request.COOKIES.get('visited')
		if visited:
			response =HttpResponse('welcome back!')
		else:
			response=HttpResponse('welcome to my website!')
			response.set_cookie('visited',True,path='/',)
		return response

def documents_ia_Kanask(request):
    template_name ='api/api_detail.html'
    
    json_path='api_hexa_path.json'
    
    with open(json_path,'r') as json_file:
        dados=json.load(json_file)
   
    return JsonResponse({'dados': dados})