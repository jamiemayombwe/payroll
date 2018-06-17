from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView

from payapp.forms.pay_roll_form import PayRollForm
from payapp.models.pay_roll import PayRoll


@method_decorator(login_required, name='dispatch')
class PayRollListView(ListView):
    template_name = 'pay_rolls.html'
    model = PayRoll

    def active(self):
        return 'payrolls_active'

    # def get_context_data(self, **kwargs):
    #     context = super(Home, self).get_context_data(**kwargs)
    #     context['home'] = 'home'
    #     return context


@method_decorator(login_required, name='dispatch')
class PayRollCreateView(CreateView):
    template_name = 'pay_roll_form.html'
    model = PayRoll
    form_class = PayRollForm
    # initial = {'key': 'value'}

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(self.request, self.template_name, {'form': form})

    def active(self):
        return 'payrolls_active'

    def title(self):
        return 'Create payroll'


    # def form_valid(self, form):
    #     form.save()
    #     return HttpResponseRedirect('/')
    #
    # def form_invalid(self, form):
    #     return render(self.request, self.template_name, {'form': form})
