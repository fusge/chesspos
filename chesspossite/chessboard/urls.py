from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Chessboard'),
    path('about/', views.about, name='Chessboard-About')
]
