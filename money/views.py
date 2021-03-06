from django.shortcuts import redirect, render

from .models import ExpenseArticle
from django.db.models import Sum
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from .forms import ExpenseArticleForm

def index(request):
    today_date = date.today()
    # Fetch all Expense articles
    expenses_form = ExpenseArticleForm(prefix='expense')
    articles = ExpenseArticle.objects.all()
    
    # Fetch all articles of today and their sum
    articles_today = ExpenseArticle.objects.filter(date__date=today_date)
    expenses_today = articles_today.aggregate(Sum('amount'))['amount__sum']

    # Fetch articles for last month
    start_last_month_date = datetime(2021, today_date.month, 15)
    next_month = today_date + relativedelta(months=1)
    articles_last_month = ExpenseArticle.objects.filter(
        date__range=(start_last_month_date, next_month))
    expenses_last_month = articles_last_month.aggregate(Sum('amount'))['amount__sum']

    # Fetch articles for last 3 months and tehir sum
    next_three_months = today_date + relativedelta(months=3)
    articles_last_threee_month = ExpenseArticle.objects.filter(
        date__range=(start_last_month_date, next_three_months))
    expenses_last_three_months = articles_last_threee_month.aggregate(Sum('amount'))['amount__sum']

    # Fetch all articles
    articles_total_sum = articles.aggregate(Sum('amount'))['amount__sum']

    if request.method == 'POST':
        expenses_form = ExpenseArticleForm(request.POST, prefix='expense')

        if expenses_form.is_valid():
            expenses_form.save()

            return redirect('/')

    return render(request, 'home.html',{
        'articles': articles.order_by('-date'),
        'today_date': today_date,
        'expenses_today': expenses_today,
        'expenses_last_month': expenses_last_month,
        'expenses_last_three_months': expenses_last_three_months,
        'articles_total_sum': articles_total_sum,
        'next_month': next_month,
        'expenses_form': expenses_form
    })

