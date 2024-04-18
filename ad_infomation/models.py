from django.db import models


# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    created_at = models.DateField
    updated_at = models.DateField(blank=True,null=True)

    def __str__(self):
        return f"{self.title}"


class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Image(models.Model):
    url = models.CharField(max_length=350)

    def __str__(self):
        return f"{self.url}"


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}"
