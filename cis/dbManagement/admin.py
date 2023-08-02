from django.contrib import admin
from .models import Student, Faculty

# Register your models here.
admin.register(Student, Faculty)(admin.ModelAdmin)
