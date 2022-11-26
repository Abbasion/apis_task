from django.db import models

# Create your models here.
class Stock(models.Model):
    symbol = models.AutoField(primary_key=True)
    name = models.TextField(default="",null=True,blank=True)
    price = models.IntegerField(default="",null=True,blank=True)
    change = models.FloatField(default="",null=True,blank=True)

class InsiderTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default="", null=True, blank=True)
    cost = models.FloatField(default="", null=True, blank=True)
    symbol = models.ForeignKey(Stock,on_delete=models.CASCADE)

class Valuation(models.Model):
    id = models.AutoField(primary_key=True)
    market_cap = models.IntegerField(default="",null=True,blank=True)
    pe_ratio = models.FloatField(default="", null=True, blank=True)
    symbol = models.ForeignKey(Stock,on_delete=models.CASCADE)