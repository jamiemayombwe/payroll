import datetime
import decimal

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from payapp.forms.pay_roll_form import PayRollForm
from payapp.models.employee import Employee
from payapp.models.pay_roll import PayRoll, CREATED, Deduction, PayRollItem
from payapp.services.pay_roll_service import PayRollService


@method_decorator(login_required, name='dispatch')
class PayRollListView(ListView):
    template_name = 'pay_rolls.html'
    model = PayRoll

    def active(self):
        return 'payrolls_active'


@method_decorator(login_required, name='dispatch')
class PayRollCreateView(CreateView):
    template_name = 'pay_roll_form.html'
    model = PayRoll
    form_class = PayRollForm

    def active(self):
        return 'payrolls_active'

    def title(self):
        return 'Create payroll'

    def form_valid(self, form):
        pay_roll_service = PayRollService(self.request)
        pay_roll = pay_roll_service.create_pay_roll(form)

        add_all_active_employees_to_pay_roll = form.cleaned_data['add_all_active_employees']
        if add_all_active_employees_to_pay_roll:
            local_service_tax_amount = form.cleaned_data['annual_local_service_tax_to_be_paid']
            pay_roll_service.create_pay_roll_items(pay_roll, local_service_tax_amount)

        return HttpResponseRedirect('/')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class PayRollItemsListView(ListView):
    template_name = 'pay_roll_items.html'
    model = PayRollItem

    def get_queryset(self):
        self.pay_roll = get_object_or_404(PayRoll, id=self.kwargs['pk'])
        return PayRollItem.objects.filter(pay_roll=self.pay_roll)

    def status(self):
        self.pay_roll = get_object_or_404(PayRoll, id=self.kwargs['pk'])
        return  self.pay_roll.status

    def active(self):
        return 'payrolls_active'
