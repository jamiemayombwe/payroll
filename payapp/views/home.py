from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, TemplateView


class Home(TemplateView):
    template_name = 'home.html'
    # greeting = 'hello Jamie'

    # def get(self, request):
    #     return HttpResponse()
