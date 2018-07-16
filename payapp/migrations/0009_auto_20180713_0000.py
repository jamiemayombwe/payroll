# Generated by Django 2.0.5 on 2018-07-12 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0008_auto_20180701_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payslip',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='pay_roll_item',
        ),
        migrations.AddField(
            model_name='deduction',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='payapp.Employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='paye_type',
            field=models.CharField(choices=[('paye_method_one', '0.3 * Taxable Amount'), ('paye_method_two', '25,000 + [0.3 * (Taxable Amount - 410,000)]')], max_length=100),
        ),
        migrations.DeleteModel(
            name='PaySlip',
        ),
    ]