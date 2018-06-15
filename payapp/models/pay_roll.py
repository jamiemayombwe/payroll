from django.db import models
from payapp.models.employee import Employee

PAYROLL_STATUS = (
        (1, 'Created'),
        (2, 'Authorized'),
        (3, 'Paid')
    )


class PayRoll(models.Model):
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)
    pay_date = models.DateTimeField(blank=False, null=False)
    total_amount = models.DecimalField(decimal_places=3, max_digits=15, blank=False, null=False)
    status = models.IntegerField(choices=PAYROLL_STATUS, null=False)
    created_by = models.PositiveIntegerField(null=False)
    authorized_by = models.PositiveIntegerField(null=True)
    paid_by = models.PositiveIntegerField(null=True)


class Deduction(models.Model):
    amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    created_by = models.PositiveIntegerField(null=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)


class PayRollItem(models.Model):
    pay_roll = models.ForeignKey(PayRoll, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deductions = models.ManyToManyField(Deduction)
    taxable_amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    employee_nssf_contribution = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    employer_nssf_contribution = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    nssf_amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    local_service_taxable_amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    annual_local_service_tax_paid = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    annual_local_service_tax_to_be_paid = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    net_pay = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    status = models.IntegerField(choices=PAYROLL_STATUS, null=False)
    created_by = models.PositiveIntegerField(null=False)


class PaySlip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_roll_item = models.OneToOneField(PayRoll, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    created_by = models.PositiveIntegerField(null=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
