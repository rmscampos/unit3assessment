from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
      return self.description

    def get_absolute_url(self):
      return reverse('home', kwargs={'item_id': self.id})