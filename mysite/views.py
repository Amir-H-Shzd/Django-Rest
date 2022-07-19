from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def Home_view(request):
    return HttpResponse('<h1>Hello Django</h1>')

def About_view(request):
    return HttpResponse('<h1>About</h1>')

def Contact_view(request):
    return HttpResponse('<h1>Contact</h1>')
