from django.shortcuts import render
from django.http import HttpResponse

def home(request,un,pw):
    return render(request,'a2.html')

def about(request):
    return render(request,'a1.html')    

