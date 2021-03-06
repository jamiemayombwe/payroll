# Generated by Django 2.0.5 on 2018-06-15 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='local_service_tax_amount',
            field=models.DecimalField(choices=[(100000.0, 'UGX 100,000'), (80000.0, 'UGX 80,000'), (70000.0, 'UGX 70,000')], decimal_places=3, max_digits=13),
        ),
        migrations.AlterField(
            model_name='employee',
            name='paye_type',
            field=models.CharField(choices=[('PAYE_ONE', '0.3 * Taxable Amount'), ('PAYE_TWO', '25,000 + [0.3 * (Taxable Amount - 410,000)]')], max_length=100),
        ),
    ]
