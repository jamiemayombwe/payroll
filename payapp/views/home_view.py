from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, TemplateView


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'home.html'

    def active(self):
        return 'home_active'

    # def get_context_data(self, **kwargs):
    #     context = super(Home, self).get_context_data(**kwargs)
    #     context['home'] = 'home'
    #     return context
