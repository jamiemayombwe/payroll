from django.contrib import admin

# Register your models here.
from payapp.models.deduction import Deduction
from payapp.models.employee import Employee
from payapp.models.local_service_tax import LocalServiceTax
from payapp.models.pay_roll import PayRoll, PayRollItem

admin.site.register(Employee)
admin.site.register(PayRoll)
admin.site.register(PayRollItem)
admin.site.register(Deduction)
admin.site.register(LocalServiceTax)
