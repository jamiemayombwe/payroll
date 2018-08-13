from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView

from payapp.forms.pay_roll_item_form import PayRollItemEditForm
from payapp.models.employee import Employee
from payapp.models.local_service_tax import LocalServiceTax
from payapp.models.pay_roll import PayRoll
from payapp.models.pay_roll_item import PayRollItem


@method_decorator(login_required, name='dispatch')
class PayRollItemsListView(ListView):
    template_name = 'pay_roll_items.html'
    model = PayRollItem

    def get_queryset(self):
        self.pay_roll = get_object_or_404(PayRoll, id=self.kwargs['pk'])
        return PayRollItem.objects.filter(pay_roll=self.pay_roll)

    def payroll(self):
        self.pay_roll = get_object_or_404(PayRoll, id=self.kwargs['pk'])
        return {'pay_roll': self.pay_roll}

    @property
    def active(self):
        return 'payrolls_active'


@method_decorator(login_required, name='dispatch')
class PayRollItemEditView(UpdateView):
    template_name = 'pay_roll_item_edit_form.html'
    model = PayRollItem
    form_class = PayRollItemEditForm

    def form_valid(self, form):
        pay_roll_item = PayRollItem.objects.get(id=self.kwargs["pk"])
        pay_roll_item.annual_local_service_tax_to_be_paid = form.cleaned_data["annual_local_service_tax_to_be_paid"]
        pay_roll_item.net_pay = pay_roll_item.local_service_taxable_amount - pay_roll_item.annual_local_service_tax_to_be_paid
        pay_roll_item.save()

        try:
            local_service_tax_for_this_payroll = LocalServiceTax.objects.get(payroll_id=pay_roll_item.pay_roll_id, employee_id=pay_roll_item.employee_id)
        except LocalServiceTax.DoesNotExist:
            local_service_tax_for_this_payroll = None

        if local_service_tax_for_this_payroll is not None:
            local_service_tax_for_this_payroll.amount = pay_roll_item.annual_local_service_tax_to_be_paid
            local_service_tax_for_this_payroll.save()
        else:
            employee = Employee.objects.get(id=pay_roll_item.employee_id)
            payroll = PayRoll.objects.get(id=pay_roll_item.pay_roll_id)
            local_service_tax = LocalServiceTax()
            local_service_tax.employee = employee
            local_service_tax.payroll = payroll
            local_service_tax.amount = pay_roll_item.annual_local_service_tax_to_be_paid
            local_service_tax.save()

        return HttpResponseRedirect('/payroll_items/{0}'.format(pay_roll_item.pay_roll_id))

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class BankPayRollView(ListView):
    template_name = 'bank_payroll_template.html'
    model = PayRollItem

    def get_queryset(self):
        self.pay_roll = get_object_or_404(PayRoll, id=self.kwargs['pk'])
        return PayRollItem.objects.filter(pay_roll=self.pay_roll)

    @property
    def active(self):
        return 'payrolls_active'


@method_decorator(login_required, name='dispatch')
class UraPayRollView(ListView):
    template_name = 'ura_payroll_template.html'
    model = PayRollItem

    def get_queryset(self):
        self.pay_roll = get_object_or_404(PayRoll, id=self.kwargs['pk'])
        return PayRollItem.objects.filter(pay_roll=self.pay_roll)

    @property
    def active(self):
        return 'payrolls_active'
