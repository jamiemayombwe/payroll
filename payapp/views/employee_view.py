from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from payapp.models.employee import Employee

REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', None)


@method_decorator(login_required, name='dispatch')
class EmployeeListView(ListView):
    template_name = 'employees.html'
    model = Employee

    # def get_context_data(self, **kwargs):
    #     context = super(EmployeeListView, self).get_context_data(**kwargs)
    #     all_employees = Employee.objects.all()
    #     employees_dict = {
    #         'employees': all_employees
    #     }
    #     context.update(employees_dict)
    #
    #     return context

    def active(self):
        return 'employees_active'

    def employees(self):
        return Employee.objects.all()


    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated and user.is_active:
            return super(EmployeeListView, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(REDIRECT_URL)
