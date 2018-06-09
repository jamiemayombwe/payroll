from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views import View
from django.views.generic import RedirectView


class Login(LoginView):
    template_name = 'login.html'
    success_url = 'home'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect('/payapp/')

    def form_invalid(self, form):
        return render_to_response(self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username=username, password=password)
    #
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             return HttpResponseRedirect(self.success_url)
    #         else:
    #             return HttpResponse('Your account is inactive')
    #     else:
    #         return HttpResponse('login/')


class Logout(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/payapp/login/')
    # def get(self, request):
    #     logout(request)
    #     return HttpResponseRedirect('/')
