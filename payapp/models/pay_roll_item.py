from django.db import models
from payapp.models.employee import Employee
from payapp.models.pay_roll import PayRoll


class PayRollItem(models.Model):
    pay_roll = models.ForeignKey(PayRoll, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    taxable_amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    nssf_contribution = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    pay_as_you_earn = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    local_service_taxable_amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    annual_local_service_tax_to_be_paid = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    net_pay = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '%s net pay: %s, payroll: %s' % (self.employee.name, self.net_pay, self.pay_roll)
