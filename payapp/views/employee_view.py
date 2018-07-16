from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DetailView

from payapp.forms.employee_form import EmployeeForm
from payapp.models.employee import Employee

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
        return HttpResponseRedirect('/employees/')

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
                   'phone_number': employee.phone_number, 'gross_income': employee.gross_income, 'tin': employee.tin,
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
        return HttpResponseRedirect('/employees/')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form, 'active': self.active(), 'title': self.title()})


@method_decorator(login_required, name='dispatch')
class EmployeeDetailView(DetailView):
    template_name = 'employee_detail.html'
    model = Employee

    @property
    def active(self):
        return 'employees_active'

