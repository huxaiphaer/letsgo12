from django.contrib import admin

# Register your models here.
from course import models

admin.site.register(models.Course)
admin.site.register(models.Review)
