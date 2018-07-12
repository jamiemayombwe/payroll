from django.db import models

from payapp.models.employee import Employee


class LocalServiceTax(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    year = models.IntegerField(null=False)
    amount = models.DecimalField(decimal_places=3, max_digits=13, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '%s: UGX %s in %s' % (self.employee.name, self.amount, self.year)


