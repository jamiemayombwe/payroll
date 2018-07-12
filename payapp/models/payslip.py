from django.db import models

from payapp.models.employee import Employee
from payapp.models.pay_roll import PayRoll


class PaySlip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_roll_item = models.OneToOneField(PayRoll, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    created_by = models.PositiveIntegerField(null=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)