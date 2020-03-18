from django.shortcuts import render
from django.http import HttpResponse
from  . import machine_learning_model

def home(request):
    return render(request,'index.html')

def about(request):
    user_input = request.GET['user_input']
    user_input = machine_learning_model.multiplier(user_input)
    return render(request,'about.html',{'user_input':user_input})

def contact(request):
    return render(request,'contact.html')