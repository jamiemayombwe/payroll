from django import forms

from payapp.models.employee import Employee


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    gross_income = forms.DecimalField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    tin = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    nssf_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    paye_type = forms.ChoiceField(required=True, choices=Employee.PAYE_METHODS, widget=forms.Select(attrs={'class': "form-control m-b"}))
    local_service_tax_amount = forms.ChoiceField(required=True, choices=Employee.LST_AMOUNTS, widget=forms.Select(attrs={'class': "form-control m-b"}))
    active = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Employee
        fields = ('name', 'title', 'email', 'phone_number', 'gross_income', 'tin', 'nssf_number', 'paye_type', 'local_service_tax_amount', 'active')
