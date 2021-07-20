from django.shortcuts import render
from django.http import HttpResponse
from .models import ExpenseArticle


def index(request):
    articles = ExpenseArticle.objects.all()
    
    return render(request, 'home.html',{
        'articles': articles,
    })

