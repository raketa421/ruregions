
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.main, name = 'main'),
    path('region/', views.reg, name = 'result'),
    path('search/', views.search, name = 'search')
]
