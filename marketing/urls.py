from django.urls import (include, path,)
app_name = 'marketing'


from .views import iA_ZanasK

urlpatterns = [
  path('zanask/', iA_ZanasK.as_view(), name='iA_ZanasK'),
  ]