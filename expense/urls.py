from django.urls import include, path
app_name = 'expense'
from expense.views import printing

urlpatterns = [
  path('printing/', printing, name='printing'),

]