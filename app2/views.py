from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('mister cool')
def sachin(request):
    return HttpResponse('<marquee>god of cricket</marquee>')