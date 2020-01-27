from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Company(models.Model):
    name = models.CharField(max_length=200)
    employee_number = models.IntegerField()
    established = models.IntegerField()

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Review(models.Model):
    RATING_CHOICES = (1, 2, 3, 4, 5)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=10 * 1000)
    ip_address = models.GenericIPAddressField(protocol='both')
    submission_date = models.DateTimeField(default=datetime.now)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
