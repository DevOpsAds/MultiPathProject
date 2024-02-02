from django.urls import (include, path,)
app_name = 'supplier'





from .views import (iA_ZanasK,documents_ia_Kanask,
  SuppliersCreateView,SuppliersListView,SuppliersDetailView,SuppliersUpdateView,SuppliersDeleteView,
  suppliers_list,suppliers_create,suppliers_detail,suppliers_update,suppliers_detail,supplier_delete
)

urlpatterns = [
  path('zanask/', iA_ZanasK.as_view(), name='iA_ZanasK'),
  path('zanask/documents/', documents_ia_Kanask, name='zanask_documents'),

  path('vcreate/', SuppliersCreateView.as_view(), name='SuppliersCreateView'),
  path('vlist/', SuppliersListView.as_view(), name='SuppliersListView'),
  path('vcreate/', SuppliersCreateView.as_view(), name='SuppliersCreateView'),
  path('<int:pk>/vdetail/', SuppliersDetailView.as_view(), name='SuppliersDetailView'),
  path('<int:pk>/vupdate/', SuppliersUpdateView.as_view(), name='SuppliersUpdateView'),
  path('<int:pk>/vdelete/', SuppliersDeleteView.as_view(), name='SuppliersDeleteView'),

  path('list/', suppliers_list, name='suppliers_list'),
  path('create/', suppliers_create, name='suppliers_create'),
  path('<int:pk>/detail/', suppliers_detail, name='suppliers_detail'),
  path('<int:pk>/update/', suppliers_update, name='suppliers_update'),
  path('<int:pk>/delete/', supplier_delete, name='supplier_delete'),
    
]
