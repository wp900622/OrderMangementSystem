from django.db import models


# Create your models here.
class Product(models.Model):
    quarter = models.CharField(unique=True, max_length=20, null=True, default="")
    num_of_products = models.IntegerField()
    def __str__(self):
        return f'{self.quarter} - {self.num_of_products}'

class Report(models.Model):

    Year_Quarter = models.CharField(unique=True, max_length=20,null=True, default="")
    ProductA = models.IntegerField()
    ProductB = models.IntegerField()
    ProductC = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.Year_Quarter} - {self.ProductA}-{self.ProductB}-{self.ProductC}'