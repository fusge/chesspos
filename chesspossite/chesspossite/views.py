from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is the main page of the site. Add content here!')