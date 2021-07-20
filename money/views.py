from django.shortcuts import render
from .models import ExpenseArticle
from django.db.models import Sum
from datetime import date


def index(request):
    # Fetch all Expense articles
    articles = ExpenseArticle.objects.all()
    
    # Fetch all articles of today and their sum
    today_date = date.today()
    articles_today = ExpenseArticle.objects.filter(date__date=today_date)
    expenses_today = articles_today.aggregate(Sum('amount'))['amount__sum']



    return render(request, 'home.html',{
        'articles': articles,
        'today_date': today_date,
        'expenses_today': expenses_today,
    })

