from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    ivan = 'ivan'
    return render(request, 'home.html')

