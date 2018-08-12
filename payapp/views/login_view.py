from django.contrib.auth import login
from django.contrib.auth.views import LoginView, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import RedirectView


class Login(LoginView):
    template_name = 'login.html'
    success_url = 'home'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect('/')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


class Logout(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/login/')
