from django.db import models

# Create your models here.

class EconomicEvent(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=100)  # Company ticker symbol
    source = models.CharField(max_length=255, default='Alpha Vantage')

    def __str__(self):
        return f"{self.name} ({self.company}) on {self.date}"
