# Generated by Django 2.0.5 on 2018-06-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('gross_income', models.DecimalField(decimal_places=3, max_digits=13)),
                ('tin', models.CharField(blank=True, max_length=20, null=True, verbose_name='TIN')),
                ('nssf_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='NSSF Number')),
                ('paye_type', models.CharField(choices=[('PAYE_ONE', '0.3 * Taxable Amount'), ('PAYE_TWO', '25,000 + [0.3 * (Taxable Amount - 410,000)]')], max_length=100, verbose_name='Select PAYE method for this employee')),
                ('local_service_tax_amount', models.DecimalField(choices=[(100000.0, 'UGX 100,000'), (80000.0, 'UGX 80,000'), (70000.0, 'UGX 70,000')], decimal_places=3, max_digits=13, verbose_name='Select Local Service Tax method for this employee')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
