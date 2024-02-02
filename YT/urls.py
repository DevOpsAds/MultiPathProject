from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
app_name = 'project'

from lockwell_208_land.views import printing

urlpatterns = [
  #path('create_as_p/', market_as_p, name='lockwell_create_as_p'),
  path('printing/', printing, name='printing'),

]