from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, TemplateView


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'home.html'
    # greeting = 'hello Jamie'

    # def get(self, request):
    #     return HttpResponse()
