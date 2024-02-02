from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('address/', include('address.urls', namespace='address')),

    path('', include('app.urls', namespace='app')),
    path('api/', include('api.urls', namespace='api')),
    path('crm/', include('crm.urls', namespace='crm')),
    path('expense/', include('expense.urls', namespace='expense')),
    path('eleutero/', include('eleutero.urls', namespace='eleutero')),
    path('fl2/', include('fl2.urls', namespace='fl2')),
    path('marketing/', include('marketing.urls', namespace='marketing')),
    path('supplier/', include('supplier.urls', namespace='supplier')),
    path('finance/', include('finance.urls', namespace='finance')),

    path('chip/', include('relacionChip.urls', namespace='relacionChip')),
    
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )