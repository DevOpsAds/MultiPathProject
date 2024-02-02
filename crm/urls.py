from django.urls import  path
#from django.contrib import admin

app_name = 'crm'

from crm.views import person_create, person_list, person_create1, person_create2, person_as_p,person_update, person_detaill, send_contact, PersonBootstrapCreate, PersonCrispyCreate, photo_create,person_create_ajax,person_json, person_vuejs_list, person_vuejs_create, person_vuejs_update, person_vuejs_delete

urlpatterns = [
    path('create_as_p/', person_as_p, name='create_as_p'),
    path('create/', person_create , name='person_create'),
    path('create1/', person_create1, name='person_create1'),
    path('create2/', person_create2, name='person_create2'),

    path('person_list/', person_list, name='person_list'),
    path('vuejs/', person_vuejs_list, name='person_vuejs_list'),
    path('vuejs/json/' ,person_json, name='person_json'),
    path ('vuejs/create/',person_vuejs_create, name='person_vuejs_create'),


    path('<int:pk>/', person_detaill, name='person_detail'),
    path('<int:pk>/update/', person_update, name='person_update'),
    path('contact/send' , send_contact, name= 'send_contact'),
    path('bootstrap/create/' , PersonBootstrapCreate.as_view(), name= 'person_bootstrap_create'), # noqa E501
    path('crispy/create/', PersonCrispyCreate.as_view(), name='person_crispy_create'), # noqa E501
    path('photo/create/',photo_create, name= 'photo_create'),
    
    path('create/ajax/',person_create_ajax, name='person_create_ajax'),
    path('<int:pk>/vuejs/update/', person_vuejs_update, name='person_vuejs_update'),  # noqa E501
    path('<int:pk>/vuejs/delete/', person_vuejs_delete, name='person_vuejs_delete'),  # noqa E501

]
