# coding:utf-8
from django import forms
from automechanic.service_order.models import ServiceOrder
from automechanic.employee.models import Employee


class ServiceOrderForm(forms.ModelForm):

    employees = forms.ModelMultipleChoiceField(
        Employee.objects.all(),
        widget=forms.SelectMultiple()
    )

    class Meta:
        model = ServiceOrder
