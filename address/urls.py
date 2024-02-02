from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
app_name = 'address'

from address.views import printing,address_as_p,filter_cep,ceps_ajax,address_list
urlpatterns = [
 
  path('printing/', printing, name='printing'),
  path('create/', address_as_p, name='create_as_p'),
  path('filter_cep/', filter_cep, name='filter_cep'),
  path('ceps_ajax/', ceps_ajax, name='ceps_ajax'),
   path('address_list/', address_list, name='address_list'),   
  
  
  ]