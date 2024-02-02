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





# 09/08/2023 _JB4.
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