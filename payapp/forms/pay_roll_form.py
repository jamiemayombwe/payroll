from django import forms


class PayRollForm(forms.Form):
    from_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    to_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    pay_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    add_all_active_employees = forms.BooleanField(initial=True, required=False, label='Add all active employees to this payroll')
