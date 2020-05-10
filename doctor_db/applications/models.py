from django.db import models

class Covid_tb(models.Model):
    id = models.AutoField(primary_key=True)
    age =  models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=1)
    race = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    hospital = models.CharField(max_length=30)
    covid_strain = models.CharField(max_length=1)
    pre_exisiting = models.CharField(max_length=50)
    hospitalised = models.CharField(max_length=1)
    respirator_required = models.CharField(max_length=1)
    medicine_applied = models.CharField(max_length=30)
    current_status = models.CharField(max_length=1)
    date_of_leave = models.DateTimeField()
    length_of_stay = models.IntegerField()
