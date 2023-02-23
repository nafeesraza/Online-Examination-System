from tkinter import Menu
from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    
   res=render(request,'testapp/show_test.html')
   return res
def about(request):
    res=render(request,'testapp/about.html')
    return res
def contactus(request):
    res=render(request,'testapp/contactus.html')
    return res
# Create your views here.
