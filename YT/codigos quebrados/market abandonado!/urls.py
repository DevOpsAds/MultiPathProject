from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
app_name = 'market'

from market.views import printing,market_as_p

urlpatterns = [
  path('create_as_p/', market_as_p, name='market_create_as_p'),
  path('jsi18n',JavaScriptCatalog.as_view(),name='js-catlog'),
  path('printing/', printing, name='printing'),

]