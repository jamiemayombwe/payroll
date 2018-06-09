from django.urls import path

from payapp.views.employee_view import EmployeeListView
from payapp.views.home_view import Home
from payapp.views.login_view import Login, Logout


urlpatterns = [
    # path('', views.index, name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('', Home.as_view(), name='home'),
    path('employees/', EmployeeListView.as_view(), name='employees'),
]
