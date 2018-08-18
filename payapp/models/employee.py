from django.db import models


class Employee(models.Model):
    paye_method_one = 'paye_method_one'
    paye_method_two = 'paye_method_two'
    PAYE_METHODS = (
        (paye_method_one, '0.3 * Taxable Amount'),
        (paye_method_two, '25,000 + [0.3 * (Taxable Amount - 410,000)]')
    )

    lst_one = 10000.000
    lst_two = 20000.000
    lst_three = 30000.000
    lst_four = 400000.000
    lst_five = 500000.000
    lst_six = 600000.000
    lst_seven = 700000.000
    lst_eight = 800000.000
    lst_nine = 90000.000
    lst_one_hundred = 100000.000
    LST_AMOUNTS = (
        (lst_one, 'UGX 10,000'),
        (lst_two, 'UGX 20,000'),
        (lst_three, 'UGX 30,000'),
        (lst_four, 'UGX 40,000'),
        (lst_five, 'UGX 50,000'),
        (lst_six, 'UGX 60,000'),
        (lst_seven, 'UGX 70,000'),
        (lst_eight, 'UGX 80,000'),
        (lst_nine, 'UGX 90,000'),
        (lst_one_hundred, 'UGX 100,000'),
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    gross_income = models.DecimalField(decimal_places=3, max_digits=13)
    bank_name = models.CharField(max_length=50, blank=False, null=False)
    bank_account_number = models.CharField(max_length=50, blank=False, null=False)
    tin = models.CharField(max_length=20, verbose_name='TIN', blank=True, null=True)
    nssf_number = models.CharField(max_length=20, verbose_name='NSSF Number', blank=False, null=False)
    paye_type = models.CharField(max_length=100, choices=PAYE_METHODS, blank=False, null=False)
    local_service_tax_amount = models.DecimalField(decimal_places=3, max_digits=13, choices=LST_AMOUNTS, blank=False, null=False)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

