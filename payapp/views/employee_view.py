from io import BytesIO

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.views.generic.base import View
from xhtml2pdf import pisa

from payapp.forms.employee_form import EmployeeForm
from payapp.models.employee import Employee
from payapp.models.pay_roll import PAID
from payapp.models.pay_roll_item import PayRollItem

REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', None)


@method_decorator(login_required, name='dispatch')
class EmployeeListView(ListView):
    template_name = 'employees.html'
    model = Employee

    @property
    def active(self):
        return 'employees_active'


@method_decorator(login_required, name='dispatch')
class EmployeeCreateView(CreateView):
    template_name = 'employee_form.html'
    model = Employee
    form_class = EmployeeForm

    @property
    def active(self):
        return 'employees_active'

    @property
    def title(self):
        return 'Create employee'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/employees')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class EmployeeEditView(UpdateView):
    template_name = 'employee_form.html'
    model = Employee
    form_class = EmployeeForm

    def active(self):
        return 'employees_active'

    def title(self):
        return 'Edit employee'

    def get(self, request, *args, **kwargs):
        employee = Employee.objects.get(id=kwargs['pk'])
        initial = {'name': employee.name, 'title': employee.title, 'email': employee.email,
                   'phone_number': employee.phone_number, 'gross_income': employee.gross_income,
                   'bank_name': employee.bank_name, 'bank_account_number': employee.bank_account_number, 'tin': employee.tin,
                   'nssf_number': employee.nssf_number, 'paye_type': employee.paye_type,
                   'local_service_tax_amount': employee.local_service_tax_amount, 'active': employee.active}
        if employee.local_service_tax_amount == 100000.000:
            initial['local_service_tax_amount'] = Employee.LST_AMOUNTS[0]
        if employee.local_service_tax_amount == 80000.000:
            initial['local_service_tax_amount'] = Employee.LST_AMOUNTS[1]
        if employee.local_service_tax_amount == 70000.000:
            initial['local_service_tax_amount'] = Employee.LST_AMOUNTS[2]
        form = self.form_class(initial=initial)

        return render(request, self.template_name, {'form': form, 'active': self.active(), 'title': self.title()})

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/employees')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form, 'active': self.active(), 'title': self.title()})


@method_decorator(login_required, name='dispatch')
class EmployeeDetailView(DetailView):
    template_name = 'employee_detail.html'
    model = Employee

    @property
    def active(self):
        return 'employees_active'

    def paid_payroll_items(self):
        self.employee = get_object_or_404(Employee, id=self.kwargs['pk'])
        paid_payroll_items = self.employee.payrollitem_set.filter(pay_roll__status__exact=PAID)
        return paid_payroll_items


def render_to_pdf(html_template, context={}):
    template = get_template(html_template)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@method_decorator(login_required, name='dispatch')
class PayslipPdfView(View):
    template_name = "payslip.html"
    model = PayRollItem

    def get(self, request, *args, **kwargs):
        pay_roll_item = PayRollItem.objects.get(id=kwargs['pk'])
        data = {'name': pay_roll_item.employee.name,
                'title': pay_roll_item.employee.title,
                'pay_date': pay_roll_item.pay_roll.pay_date,
                'gross_income': pay_roll_item.employee.gross_income,
                'paye_amount': pay_roll_item.pay_as_you_earn,
                'nssf_amount': pay_roll_item.nssf_contribution,
                'net_pay': pay_roll_item.net_pay
                }

        pdf = render_to_pdf(self.template_name, data)
        return HttpResponse(pdf, content_type='application/pdf')



