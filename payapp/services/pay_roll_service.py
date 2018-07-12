import datetime
import decimal

from payapp.models.deduction import Deduction
from payapp.models.employee import Employee
from payapp.models.pay_roll import PayRoll, CREATED, PayRollItem


class PayRollService(object):
    def __init__(self, request):
        self.request = request

    def create_pay_roll(self, form):
        pay_roll = PayRoll()
        pay_roll.start_date = form.cleaned_data['start_date']
        pay_roll.end_date = form.cleaned_data['end_date']
        pay_roll.pay_date = form.cleaned_data['pay_date']
        pay_roll.total_amount = 0
        pay_roll.status = CREATED
        pay_roll.created_by = self.request.user.id

        pay_roll.save()
        return pay_roll

    def create_pay_roll_items(self, pay_roll, local_service_tax_amount):
        active_employees = Employee.objects.filter(active=True)

        for employee in active_employees:
            payroll_item = PayRollItem()
            payroll_item.pay_roll = pay_roll
            payroll_item.employee = employee
            payroll_item.taxable_amount = employee.gross_income / decimal.Decimal(1.10)
            payroll_item.nssf_contribution = payroll_item.taxable_amount * decimal.Decimal(0.15)
            if employee.paye_type == Employee.paye_method_one:
                payroll_item.pay_as_you_earn = payroll_item.taxable_amount * decimal.Decimal(0.30)
            elif employee.paye_type == Employee.paye_method_two:
                payroll_item.pay_as_you_earn = 25000 + ((payroll_item.taxable_amount - 410000) * decimal.Decimal(0.30))
            payroll_item.local_service_taxable_amount = employee.gross_income - payroll_item.nssf_contribution - payroll_item.pay_as_you_earn

            if local_service_tax_amount is not None and local_service_tax_amount > 0:
                payroll_item.annual_local_service_tax_to_be_paid = decimal.Decimal(local_service_tax_amount)
            else:
                payroll_item.annual_local_service_tax_to_be_paid = decimal.Decimal(0.00)
            payroll_item.status = CREATED
            payroll_item.created_by = self.request.user.id

            employee_deductions = Deduction.objects.filter(status=Deduction.NOT_PAID).order_by('-created_date')
            if employee_deductions:
                employee_deduction = Deduction.objects.filter(status=Deduction.NOT_PAID).order_by('-created_date')[0]
                employee_deduction_month = employee_deduction.created_date.month
                employee_deduction_year = employee_deduction.created_date.year

                today = datetime.date.today()
                today_month = today.month
                today_year = today.year

                if (employee_deduction_year == today_year and today_month - employee_deduction_month == 1) or (
                        today_year - employee_deduction_year == 1 and employee_deduction_month - today_month == 1):
                    payroll_item.net_pay = payroll_item.local_service_taxable_amount - payroll_item.annual_local_service_tax_to_be_paid - employee_deduction.amount

                    employee_deduction.status = Deduction.PAID
                    employee_deduction.save()
            else:
                payroll_item.net_pay = payroll_item.local_service_taxable_amount - payroll_item.annual_local_service_tax_to_be_paid

            payroll_item.save()

            payroll_items = PayRollItem.objects.filter(pay_roll=pay_roll)

            for item in payroll_items:
                pay_roll.total_amount = pay_roll.total_amount + item.net_pay

            pay_roll.save()
