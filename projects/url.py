from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('home/<str:un>/<str:pw>',views.home, name='home'),
    path('about/',views.about, name='about'),
]
