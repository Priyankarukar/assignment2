from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
def homepage(request):
    f1=forms.MyForm()
    return render(request,"home.html",{'form':f1})