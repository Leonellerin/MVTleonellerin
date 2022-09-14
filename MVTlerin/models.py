from django.db import models


class padre(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField


class madre(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField


class hermano(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField
