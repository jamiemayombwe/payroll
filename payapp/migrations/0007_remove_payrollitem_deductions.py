# Generated by Django 2.0.5 on 2018-06-30 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0006_auto_20180630_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payrollitem',
            name='deductions',
        ),
    ]