from django import forms

from payapp.models.pay_roll import PayRollItem


class PayRollItemEditForm(forms.ModelForm):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    annual_local_service_tax_to_be_paid = forms.DecimalField(required=True, label='Local Service Tax amount to be paid',
                                                  widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = PayRollItem
        fields = ("id", "annual_local_service_tax_to_be_paid")
