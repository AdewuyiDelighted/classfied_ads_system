from django.db import models


# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    created_at = models.DateField
    updated_at = models.DateField


class Location(models.Model):
    name = models.CharField(max_length=100)


class Image(models.Model):
    url = models.CharField(max_length=350)


class Category(models.Model):
    name = models.CharField(max_length=25)