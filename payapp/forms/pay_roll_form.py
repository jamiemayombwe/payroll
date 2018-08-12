from django import forms

from payapp.models.pay_roll import PayRoll


class PayRollForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    prepared_by = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    start_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': "form-control"}))
    end_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    pay_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = PayRoll
        fields = ('id', 'prepared_by', 'start_date', 'end_date', 'pay_date')

    def clean(self):
        id = self.cleaned_data['id']
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        pay_date = self.cleaned_data['pay_date']

        if len(id) == 0:
            pay_rolls = PayRoll.objects.order_by('-end_date')
            if pay_rolls:
                last_pay_roll = PayRoll.objects.order_by('-end_date')[0]

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


class PayRollAuthorizeForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    authorized_by = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = PayRoll
        fields = ("id", "authorized_by")


class PayRollApproveForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    approved_by = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = PayRoll
        fields = ("id", "approved_by")