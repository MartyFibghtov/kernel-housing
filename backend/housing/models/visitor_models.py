from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=100)
