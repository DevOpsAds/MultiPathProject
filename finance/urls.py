from django.urls import include, path
app_name = 'finance'
from finance.views import printing

urlpatterns = [
  path('printing/', printing, name='printing'),

]