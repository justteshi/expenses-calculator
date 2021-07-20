from django.db import models

# Create your models here.

class ExpenseArticle(models.Model):
    amount = models.CharField(max_length=25)
    reason = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)