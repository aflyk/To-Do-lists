from django.shortcuts import render
from django.http import HttpResponse

def home_page(requests):
    """домашняя страница"""

    return HttpResponse("Hello world")