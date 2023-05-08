from django.db import models


class Professional(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    date_of_birth = models.DateField()
    industry = models.CharField(max_length=100, null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
