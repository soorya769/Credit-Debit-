# journal_app/models.py
from django.db import models

class JournalEntry(models.Model):
    date = models.DateField()
    parti = models.CharField(max_length=255)
    particulars = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
