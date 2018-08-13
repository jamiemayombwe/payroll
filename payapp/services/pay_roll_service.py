import datetime
import decimal

from payapp.models.deduction import Deduction
from payapp.models.employee import Employee
from payapp.models.pay_roll import PayRoll, CREATED
from payapp.models.pay_roll_item import PayRollItem
from payapp.viewmodels.pay_roll_view_model import PayRollViewModel


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
        pay_roll.prepared_by = form.cleaned_data['prepared_by']

        pay_roll.save()
        return pay_roll

    def create_pay_roll_items(self, pay_roll):
        active_employees = Employee.objects.filter(active=True)

        for employee in active_employees:
            try:
                employee_pay_roll_item = PayRollItem.objects.get(pay_roll_id=pay_roll.id, employee_id=employee.id)
            except PayRollItem.DoesNotExist:
                employee_pay_roll_item = None

            if employee_pay_roll_item is None:
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
                payroll_item.annual_local_service_tax_to_be_paid = decimal.Decimal(0.00)
                payroll_item.status = CREATED

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

                        employee_deduction.status = Deduction.PENDING
                        employee_deduction.save()
                else:
                    payroll_item.net_pay = payroll_item.local_service_taxable_amount - payroll_item.annual_local_service_tax_to_be_paid

                payroll_item.save()

    def get_pay_roll_view_models(self):
        pay_rolls = PayRoll.objects.all()
        pay_roll_view_models = []

        if len(pay_rolls) > 0:
            for pay_roll in pay_rolls:
                total_net_pay = decimal.Decimal(0.00)
                pay_roll_items = pay_roll.payrollitem_set.all()
                for pay_roll_item in pay_roll_items:
                    total_net_pay = total_net_pay + pay_roll_item.net_pay

                pay_roll_view_model = PayRollViewModel(
                    pay_roll.id,
                    pay_roll.start_date,
                    pay_roll.end_date,
                    pay_roll.pay_date,
                    pay_roll.prepared_by,
                    pay_roll.authorized_by,
                    pay_roll.approved_by,
                    pay_roll.status,
                    pay_roll.get_status_display(),
                    total_net_pay)
                pay_roll_view_models.append(pay_roll_view_model)
        return pay_roll_view_models

    def update_pay_roll(self, form, pay_roll_id):
        pay_roll = PayRoll.objects.get(id=pay_roll_id)

        if pay_roll is not None:
            pay_roll.prepared_by = form.cleaned_data['prepared_by']
            pay_roll.start_date = form.cleaned_data['start_date']
            pay_roll.end_date = form.cleaned_data['end_date']
            pay_roll.pay_date = form.cleaned_data['pay_date']

            pay_roll.save()
