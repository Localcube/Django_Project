from django.db import models

class Boot(models.Model):

    name = models.CharField(max_length=100)
    adreess = models.CharField(max_length=200)


def __str__(self):
  return self.name

