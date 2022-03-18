from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo_url = models.CharField(max_length=200)
    discount = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = 'product'