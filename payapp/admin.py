from django.contrib import admin

# Register your models here.
from payapp.models.employee import Employee

admin.site.register(Employee)
