from django.shortcuts import render
from . models import *
# Create your views here.
def adhome (request):
    return render (request,'gmadmin/adhome.html')

def application (request):
    return render (request, 'gmadmin/applications.html')