from django.db import models

from payapp.models.employee import Employee


class Deduction(models.Model):
    PAID = 1
    NOT_PAID = 2
    DEDUCTION_STATUS = ((PAID, 'Paid'), (NOT_PAID, 'Not paid'))

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    created_by = models.PositiveIntegerField(blank=True, null=False)
    status = models.IntegerField(choices=DEDUCTION_STATUS, null=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '%s: UGX %s on %s' % (self.employee.name, self.amount, self.created_date)


