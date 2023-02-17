from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'chessboard/chessboard.html', {'title': 'board'})


def about(request):
    return render(request, 'chessboard/about.html', {'title': 'About'})
