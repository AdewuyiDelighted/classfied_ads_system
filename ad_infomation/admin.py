from django.contrib import admin

from . import models


# Register your models here.


@admin.register(models.Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['title']




