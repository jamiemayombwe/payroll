from django import forms

from payapp.models.pay_roll import PayRoll


class PayRollForm(forms.ModelForm):
    start_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    end_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    pay_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    add_all_active_employees = forms.BooleanField(initial=True, required=False, label='Add all active employees to this payroll', widget=forms.CheckboxInput(attrs={'class': "i-checks"}))

    class Meta:
        model = PayRoll
        fields = ('start_date', 'end_date', 'pay_date')
