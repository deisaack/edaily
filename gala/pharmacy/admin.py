from django.contrib import admin
from . import models

admin.site.register(models.Disease)
admin.site.register(models.Drug)
admin.site.register(models.Staff)
admin.site.register(models.USSDQuery)
admin.site.register(models.Pharmacy)
