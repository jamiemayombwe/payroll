from django.db import models


class Employee(models.Model):
    paye_method_one = 'paye_method_one'
    paye_method_two = 'paye_method_two'
    PAYE_METHODS = (
        (paye_method_one, '0.3 * Taxable Amount'),
        (paye_method_two, '25,000 + [0.3 * (Taxable Amount - 410,000)]')
    )

    lst_one = 100000.000
    lst_two = 80000.000
    lst_three = 70000.000
    LST_AMOUNTS = (
        (lst_one, 'UGX 100,000'),
        (lst_two, 'UGX 80,000'),
        (lst_three, 'UGX 70,000')
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    gross_income = models.DecimalField(decimal_places=3, max_digits=13)
    bank_name = models.CharField(max_length=50, blank=False, null=False)
    bank_account_number = models.CharField(max_length=50, blank=False, null=False)
    tin = models.CharField(max_length=20, verbose_name='TIN', blank=False, null=False)
    nssf_number = models.CharField(max_length=20, verbose_name='NSSF Number', blank=False, null=False)
    paye_type = models.CharField(max_length=100, choices=PAYE_METHODS, blank=False, null=False)
    local_service_tax_amount = models.DecimalField(decimal_places=3, max_digits=13, choices=LST_AMOUNTS, blank=False, null=False)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

