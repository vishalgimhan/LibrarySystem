from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "index.html", context={"current_tab": "home"})

def shopping(request):
    return HttpResponse("welcome to shopping")

def save_student(request):
    Student_name = request.POST['Student_name']
    return render(request, "Welcome.html", context={'Student_name': Student_name})
