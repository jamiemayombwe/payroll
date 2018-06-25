from django.urls import path

from payapp.views.employee_view import EmployeeListView, EmployeeEditView, EmployeeCreateView, EmployeeDetailView
from payapp.views.login_view import Login, Logout
from payapp.views.pay_roll_view import PayRollListView, PayRollCreateView

urlpatterns = [
    # path('', views.index, name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    path('', PayRollListView.as_view(), name='payrolls'),
    path('create_payroll/', PayRollCreateView.as_view(), name='create_payroll'),
    # path('edit_payroll/<int:pk>', PayRollEditView.as_view(), name='edit_payroll'),

    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('edit_employee/<int:pk>/', EmployeeEditView.as_view(), name='edit_employee'),
    path('create_employee/', EmployeeCreateView.as_view(), name='create_employee'),
    path('employee_detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
]
