from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('home/<int:id>',views.home, name='home'),
    path('',views.about, name='about'),
]
