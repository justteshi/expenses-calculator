from django.shortcuts import render
from .models import ExpenseArticle
from django.db.models import Sum
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

def index(request):
    today_date = date.today()
    # Fetch all Expense articles
    articles = ExpenseArticle.objects.all()
    
    # Fetch all articles of today and their sum
    articles_today = ExpenseArticle.objects.filter(date__date=today_date)
    expenses_today = articles_today.aggregate(Sum('amount'))['amount__sum']

    # Fetch articles for last month
    next_month = today_date + relativedelta(months=1)

    
    return render(request, 'home.html',{
        'articles': articles.order_by('-date'),
        'today_date': today_date,
        'expenses_today': expenses_today,
        'next_month': next_month
    })

