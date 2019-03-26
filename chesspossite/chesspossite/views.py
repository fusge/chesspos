from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is the main page of the site. Add content here!')

def about(request):
    return HttpResponse('This is the about page of the site.')