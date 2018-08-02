from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from payapp.forms.pay_roll_form import PayRollForm
from payapp.models.pay_roll import PayRoll, PayRollItem, AUTHORIZED, PAID
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

    def active(self):
        return 'payrolls_active'

    def title(self):
        return 'Create payroll'

    def form_valid(self, form):
        pay_roll_service = PayRollService(self.request)
        pay_roll = pay_roll_service.create_pay_roll(form)
        pay_roll_service.create_pay_roll_items(pay_roll)

        return HttpResponseRedirect('/')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form, 'active': 'payrolls_active', 'title': 'Create payroll'})


@method_decorator(login_required, name='dispatch')
class PayRollEditView(UpdateView):
    template_name = 'pay_roll_form.html'
    model = PayRoll
    form_class = PayRollForm

    def active(self):
        return 'payrolls_active'

    def title(self):
        return 'Edit payroll'

    def get(self, request, *args, **kwargs):
        payroll = PayRoll.objects.get(id=kwargs['pk'])
        date_format = "%m/%d/%Y"
        initial = {
            'id': payroll.id,
            'start_date': payroll.start_date.strftime(date_format),
            'end_date': payroll.end_date.strftime(date_format),
            'pay_date': payroll.pay_date.strftime(date_format)
        }

        form = self.form_class(initial=initial)

        return render(request, self.template_name, {'form': form, 'active': self.active(), 'title': self.title()})

    def form_valid(self, form):
        pay_roll_service = PayRollService(self.request)
        pay_roll_service.update_pay_roll(form, self.kwargs['pk'])

        pay_roll = PayRoll.objects.get(id=self.kwargs['pk'])
        pay_roll_service.create_pay_roll_items(pay_roll)

        return HttpResponseRedirect('/')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form, 'active': 'payrolls_active', 'title': 'Edit payroll'})


@method_decorator(login_required, name='dispatch')
class PayRollDeleteView(DeleteView):
    model = PayRoll
    template_name = "confirm_delete.html"
    success_url = "/"


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


# @method_decorator(login_required, name='dispatch')
# class PayRollItemEditView(UpdateView):
#     template_name = 'pay_roll_item_form.html'
#     model = PayRollItem
#     form_class = PayRollItemForm
#
#     def get(self, request, *args, **kwargs):
#         payroll = PayRoll.objects.get(id=kwargs['pk'])
#         date_format = "%m/%d/%Y"
#         initial = {
#             'id': payroll.id,
#             'start_date': payroll.start_date.strftime(date_format),
#             'end_date': payroll.end_date.strftime(date_format),
#             'pay_date': payroll.pay_date.strftime(date_format)
#         }
#
#         form = self.form_class(initial=initial)
#
#         return render(request, self.template_name, {'form': form, 'active': self.active(), 'title': self.title()})
#
#     def form_valid(self, form):
#         pay_roll_service = PayRollService(self.request)
#         pay_roll_service.update_pay_roll(form, self.kwargs['pk'])
#
#         pay_roll = PayRoll.objects.get(id=self.kwargs['pk'])
#         pay_roll_service.create_pay_roll_items(pay_roll)
#
#         return HttpResponseRedirect('/')
#
#     def form_invalid(self, form):
#         return render(self.request, self.template_name, {'form': form, 'active': 'payrolls_active', 'title': 'Edit payroll'})


@login_required()
def authorize_payroll(request, pk):
    pay_roll = get_object_or_404(PayRoll, id=pk)

    if pay_roll is not None:
        pay_roll.status = AUTHORIZED
        pay_roll.save()

        return HttpResponseRedirect('/payroll_items/{0}'.format(pk))
    else:
        return HttpResponseRedirect('/')


# @login_required()
# def mark_payroll_as_paid(request, pk):
#     pay_roll = get_object_or_404(PayRoll, id=pk)
#
#     if pay_roll is not None:
#         pay_roll.status = PAID
#         pay_roll.save()
#
#         return HttpResponseRedirect('/payroll_items/{0}'.format(pk))
#     else:
#         return HttpResponseRedirect('/')
#
