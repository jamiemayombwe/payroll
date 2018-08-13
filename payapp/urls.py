from django.urls import path

from payapp.views import views
from payapp.views.employee_view import EmployeeListView, EmployeeEditView, EmployeeCreateView, EmployeeDetailView, \
    PayslipPdfView
from payapp.views.login_view import Login, Logout
from payapp.views.pay_roll_item_view import BankPayRollView, UraPayRollView, PayRollItemsListView, PayRollItemEditView
from payapp.views.pay_roll_view import PayRollListView, PayRollCreateView, PayRollEditView, \
    PayRollDeleteView, PayRollAuthorizeView, PayRollApproveView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    path('', PayRollListView.as_view(), name='payrolls'),
    path('create_payroll', PayRollCreateView.as_view(), name='create_payroll'),
    path('edit_payroll/<int:pk>', PayRollEditView.as_view(), name='edit_payroll'),
    path('delete_payroll/<int:pk>', PayRollDeleteView.as_view(), name='delete_payroll'),

    path('authorize_payroll/<int:pk>', PayRollAuthorizeView.as_view(), name='authorize_payroll'),
    path('approve_payroll/<int:pk>', PayRollApproveView.as_view(), name='approve_payroll'),

    path('payroll_items/<int:pk>', PayRollItemsListView.as_view(), name='payroll_items'),
    path('edit_payroll_item/<int:pk>', PayRollItemEditView.as_view(), name='edit_payroll_item'),
    path('bank_payroll_view/<int:pk>', BankPayRollView.as_view(), name='bank_payroll_view'),
    path('ura_payroll_view/<int:pk>', UraPayRollView.as_view(), name='ura_payroll_view'),


    path('employees', EmployeeListView.as_view(), name='employees'),
    path('create_employee', EmployeeCreateView.as_view(), name='create_employee'),
    path('edit_employee/<int:pk>', EmployeeEditView.as_view(), name='edit_employee'),
    path('employee_detail/<int:pk>', EmployeeDetailView.as_view(), name='employee_detail'),
    path('payslip_pdf_download/<int:pk>', PayslipPdfView.as_view(), name='payslip_pdf_download')

]
