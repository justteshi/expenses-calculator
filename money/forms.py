from django.forms import ModelForm, Select, Form, fields
from django import forms
from .models import ExpenseArticle

class ExpenseArticleForm(ModelForm):
    reason = forms.CharField(
        label='Reason',
        widget=forms.TextInput(attrs={'class':'p-4 w-full rounded-lg', 'placeholder': 'Reason'})
    )
    amount = forms.CharField(
        label='Amount',
        widget=forms.TextInput(attrs={'class':'p-4 w-full rounded-lg', 'placeholder': 'Amount in лв.'})
    )

    class Meta:
        model = ExpenseArticle
        fields = ['reason', 'amount']
