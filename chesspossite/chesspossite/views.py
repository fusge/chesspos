from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'chesspossite/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'chesspossite/about.html', {'title': 'About'})
