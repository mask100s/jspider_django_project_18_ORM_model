from django.db import models

# Create your models here.
class Country(models.Model):
  ctid=models.PositiveIntegerField(primary_key=True)
  ctname=models.CharField(max_length=100)

  
class Capital(models.Model):
  ctid=models.OneToOneField(Country,on_delete=models.CASCADE)
  cpname=models.CharField(max_length=100)
  population=models.IntegerField()