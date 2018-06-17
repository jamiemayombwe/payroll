from django.contrib import admin

# Register your models here.
from payapp.models.employee import Employee
from payapp.models.pay_roll import PayRoll

admin.site.register(Employee)
admin.site.register(PayRoll)
