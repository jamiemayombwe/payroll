from django import forms

from payapp.models.pay_roll import PayRoll


class PayRollForm(forms.ModelForm):
    start_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    end_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    pay_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    add_all_active_employees = forms.BooleanField(initial=True, required=False, label='Add all active employees to this payroll', widget=forms.CheckboxInput(attrs={'class': "i-checks"}))

    class Meta:
        model = PayRoll
        fields = ('start_date', 'end_date', 'pay_date', 'add_all_active_employees')

    def clean(self):
        # cleaned_data = super(PayRollForm, self).clean()
        form_data = self.cleaned_data
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        pay_date = self.cleaned_data['pay_date']

        last_pay_roll = PayRoll.objects.order_by('created_date')[0]

        if last_pay_roll is not None:
            if last_pay_roll.end_date > start_date:
                self.add_error('start_date', 'There is already a payroll that includes this date')

        if end_date < start_date:
            self.add_error('end_date', "End date can't be before start date")

        elif pay_date < start_date:
            self.add_error('pay_date', "Pay date can't be before start date")

        elif pay_date < end_date:
            self.add_error('pay_date', "Pay date can't be before end date")

        return self.cleaned_data
