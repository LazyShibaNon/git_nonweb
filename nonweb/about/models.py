from django.db import models

# Create your models here.

class Reviews(models.Model):
    auther = models.CharField(max_length=20)
    grade = models.IntegerField(default=0)
    comment = models.TextField()
    review_date = models.CharField(max_length=20)
    creat_date = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = "reviews"
