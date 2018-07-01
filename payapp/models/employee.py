from django.db import models


class Employee(models.Model):
    PAYE_ONE = 'PAYE_ONE'
    PAYE_TWO = 'PAYE_TWO'
    PAYE_METHODS = (
        (PAYE_ONE, '0.3 * Taxable Amount'),
        (PAYE_TWO, '25,000 + [0.3 * (Taxable Amount - 410,000)]')
    )

    LST_ONE = 100000.000
    LST_TWO = 80000.000
    LST_THREE = 70000.000
    LST_AMOUNTS = (
        (LST_ONE, 'UGX 100,000'),
        (LST_TWO, 'UGX 80,000'),
        (LST_THREE, 'UGX 70,000')
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    gross_income = models.DecimalField(decimal_places=3, max_digits=13)
    tin = models.CharField(max_length=20, verbose_name='TIN', blank=True, null=True)
    nssf_number = models.CharField(max_length=20, verbose_name='NSSF Number', blank=True, null=True)
    paye_type = models.CharField(max_length=100, choices=PAYE_METHODS, blank=False, null=False)
    local_service_tax_amount = models.DecimalField(decimal_places=3, max_digits=13, choices=LST_AMOUNTS, blank=False, null=False)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

