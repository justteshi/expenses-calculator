from django.contrib import admin
from .models import ExpenseArticle
# Register your models here.


@admin.register(ExpenseArticle)
class ExpenseArticleAdmin(admin.ModelAdmin):
    list_display = ('reason', 'amount', 'date')