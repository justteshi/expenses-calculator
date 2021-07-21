from django.forms import ModelForm, Select, Form, fields
from django import forms
from .models import ExpenseArticle

class ExpenseArticleForm(ModelForm):
    reason = forms.CharField(
        label='Reason',
        widget=forms.TextInput(
            attrs={'class':'p-4 w-full rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600', 'placeholder': 'Reason'})
    )
    amount = forms.CharField(
        label='Amount',
        widget=forms.TextInput(attrs={'class':'p-4 w-full rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600', 'placeholder': 'Amount in лв.'})
    )

    class Meta:
        model = ExpenseArticle
        fields = ['reason', 'amount']
