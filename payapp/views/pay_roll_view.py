from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView

from payapp.forms.pay_roll_form import PayRollForm
from payapp.models.pay_roll import PayRoll, PayRollItem
from payapp.services.pay_roll_service import PayRollService


@method_decorator(login_required, name='dispatch')
class PayRollListView(ListView):
    template_name = 'pay_rolls.html'
    model = PayRoll

    @property
    def active(self):
        return 'payrolls_active'

    def get_queryset(self):
        pay_roll_service = PayRollService(self.request)
        return pay_roll_service.get_pay_roll_view_models()


@method_decorator(login_required, name='dispatch')
class PayRollCreateView(CreateView):
    template_name = 'pay_roll_form.html'
    model = PayRoll
    form_class = PayRollForm

    @property
    def active(self):
        return 'payrolls_active'

    @property
    def title(self):
        return 'Create payroll'

    def form_valid(self, form):
        pay_roll_service = PayRollService(self.request)
        pay_roll = pay_roll_service.create_pay_roll(form)
        pay_roll_service.create_pay_roll_items(pay_roll)

        return HttpResponseRedirect('/')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class PayRollEditView(UpdateView):
    template_name = 'pay_roll_form.html'
    model = PayRoll
    form_class = PayRollForm

    @property
    def active(self):
        return 'payrolls_active'

    @property
    def title(self):
        return 'Edit payroll'

    def form_valid(self, form):
        pay_roll_service = PayRollService(self.request)
        pay_roll_service.update_pay_roll(form, self.kwargs['pk'])

        pay_roll = PayRoll.objects.get(id=self.kwargs['pk'])
        pay_roll_service.create_pay_roll_items(pay_roll)

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
        return self.pay_roll.status

    @property
    def active(self):
        return 'payrolls_active'
