# journal_app/forms.py
from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['date', 'parti', 'particulars', 'debit', 'credit']
