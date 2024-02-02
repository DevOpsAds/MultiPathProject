from django.urls import include, path
app_name = 'app'
from app.views import (home, create, store, painel, dologin, dashboard, password, dopassword,logout_view)

urlpatterns = [

    path('', home),
    path('create/', create),
    path('store/', store),
    path('painel/', painel),
    path('dologin/', dologin),
    path('dashboard/', dashboard,name='dashboard'),
    path('password/', password),
    path('dopassword/', dopassword),
    path('logout/',logout_view,name='logout'),
]