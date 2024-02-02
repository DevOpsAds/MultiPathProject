from django.urls import (include, path,)
app_name = 'api'





from .views import (ApiCronomentView,
  iA_ZanasK,documents_ia_Kanask,
  ApiCreateView,
)

urlpatterns = [
  path('zanask/', iA_ZanasK.as_view(), name='iA_ZanasK'),
  path('zanask/documents/', documents_ia_Kanask, name='zanask_documents'),
  path('vcronoment/', ApiCronomentView.as_view(), name='ApiCronomentView'),

  path('vcreate/', ApiCreateView.as_view(), name='ApiCreateView'),

    
]
