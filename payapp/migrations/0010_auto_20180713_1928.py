# Generated by Django 2.0.5 on 2018-07-13 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0009_auto_20180713_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalServiceTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=3, max_digits=13)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payapp.Employee')),
            ],
        ),
        migrations.RemoveField(
            model_name='payroll',
            name='total_amount',
        ),
    ]
