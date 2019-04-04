from django.db import models
import time, datetime
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    pub_date = models.DateField(default=datetime.datetime.now, blank=True)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField(default='')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pubdatepretty(self):
        return self.pub_date.strftime("%Y-%m-%d")
