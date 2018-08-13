from django.db import models

CREATED = 1
AUTHORIZED = 2
PAID = 3
PAYROLL_STATUS = (
    (CREATED, 'Created'),
    (AUTHORIZED, 'Authorized'),
    (PAID, 'Paid')
)


class PayRoll(models.Model):
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    pay_date = models.DateField(blank=False, null=False)
    status = models.IntegerField(choices=PAYROLL_STATUS, null=False)
    prepared_by = models.CharField(max_length=100, blank=False, null=False)
    authorized_by = models.CharField(max_length=100, blank=False, null=True)
    approved_by = models.CharField(max_length=100, blank=False, null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return 'From: %s To: %s' % (self.start_date, self.end_date)

