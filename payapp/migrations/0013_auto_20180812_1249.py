# Generated by Django 2.0.5 on 2018-08-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0012_auto_20180803_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='authorized_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='paid_by',
            field=models.CharField(max_length=100, null=True),
        ),
    ]