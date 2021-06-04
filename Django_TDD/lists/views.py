from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    """Домашняя страница"""
    return render(request, 'home.html')
