from django.urls import (include, path,)
from django.views.i18n import JavaScriptCatalog
app_name = 'suppliers'



from suppliers.controller import (printing,
pd_redirect)

from suppliers.views import (
filter_cep,suppliers_as_p_mod,SuppliersSitCadModelCreate,ListaBairrosView,ListaBairrosView2,
suppliers_list,suppliers_create,suppliers_detail,suppliers_update,suppliers_delete,
SuppliersCreateView,
suppliers_as_p,suppliers_save_p,suppliers_detaill,
suppliers_det_informat,
suppliers_update_p,
)

#suppliers_as_p : importe para testar
urlpatterns = [
  #path('create_as_p/', market_as_p, name='lockwell_create_as_p'),
  path('create/off', suppliers_as_p, name='supplier_create'),
  path('list/', suppliers_list, name='suppliers_list'),
  path('create/', suppliers_create, name='suppliers_create'),
  path('<int:pk>/detail/', suppliers_detail, name='suppliers_detail'),
  path('<int:pk>/update/', suppliers_update, name='suppliers_update'),
  path('<int:pk>/delete/', suppliers_update, name='suppliers_delete'),
  
  path('v.create/', SuppliersCreateView.as_view(), name='SuppliersCreateView'),
  
  path('printing/', printing, name='printing'),
  path('text/', pd_redirect, name='pd_redirect'),
  path('filter_cep/', filter_cep, name='filter_cep'),
  path('create_mod/', suppliers_as_p_mod, name='suppliers_as_p_mod'),
  path('suppliers_search/', suppliers_list, name='suppliers_search'),
  path('save_supplier/',suppliers_save_p, name='suppliers_save'),
  path('<int:pk>/', suppliers_detaill, name='supplliers_detail'),
  path('<int:pk>/information/',suppliers_det_informat, name='detail_data'),
  path('update_supplier/',suppliers_update_p, name='suppliers_update'),
  path('modal/sit_cat/', SuppliersSitCadModelCreate.as_view(), name='suppliers_sit_cat'),
  path('bairros/', ListaBairrosView.as_view(), name='ListaBairrosView'),
  path('filterboss/', ListaBairrosView2.as_view(), name='ListaBairrosView2'),  
]
