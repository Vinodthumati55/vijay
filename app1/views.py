from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return HttpResponse('rohit the hit man')
def kohli(request):
    return HttpResponse('king kohli')
