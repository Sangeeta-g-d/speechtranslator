from django.urls import path,include
from . import views
from django.contrib import admin


urlpatterns = [
    
    path('', views.translate, name='translate'),
     path('translate/', views.translate, name='translate'),

]