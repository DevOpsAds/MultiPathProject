from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.urls import include, path

urlpatterns = [
    path('', include('app.urls', namespace='app')),
    path('crm/', include('crm.urls', namespace='crm')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )