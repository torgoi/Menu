from django.db import models

class Dkango(models.Model):
    title = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.title

# Create your models here.
