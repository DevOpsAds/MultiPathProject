from django.urls import include, path
from django.views.i18n import JavaScriptCatalog

app_name = 'relacionChip'

from relacionChip.views import printing,chip_as_p,manual_m,pd_redirect,filter_list,cities_ajax,districts_ajax,filter_dropdown,city_choices_ajax,districts_choices_ajax,filter_dropdown2

from crm.views import  person_list
from crm import  views


urlpatterns = [
  path('crm/',include('crm.urls')),

  path('chip/', chip_as_p, name='chip_as_p'),
  path('printing/', printing, name='printing'),
  path('manual/', manual_m, name='manual_m'),
  path('pd_redirect/', pd_redirect, name='red'),
  
  path('filter_list/',filter_list,name='filter_list'),
  path('cities_ajax/',cities_ajax,name='cities_ajax'),
  path('districts_ajax/',districts_ajax,name='districts_ajax'),

  path('filter_dropdown/',filter_dropdown,name='filter_dropdown'),
  path('city_choices_ajax',city_choices_ajax,name='cities_choices_ajax'),
  path('districts_choices_ajax',districts_choices_ajax,name='districts_choices_ajax'),
  #drop com mais django
  path('filter_dropdown2/',filter_dropdown2,name='filter_dropdown2'),

  #filtro agregador de endereço,#buscando kit completo
    path('person_list/', person_list, name='person_list'),
  
  
 

]