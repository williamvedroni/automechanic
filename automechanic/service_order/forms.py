# coding:utf-8
from django import forms
from automechanic.service_order.models import ServiceOrder
from automechanic.employee.models import Employee
from automechanic.authentication.client.models import Client
from automechanic.part.models import Part
from automechanic.messages import error_messages, date_error_messages


class ServiceOrderForm(forms.ModelForm):

    employees = forms.ModelMultipleChoiceField(
        Employee.objects.all(),
        widget=forms.SelectMultiple()
    )

    clients = forms.ModelChoiceField(
        Client.objects.all(),
    )

    parts = forms.ModelMultipleChoiceField(
        Part.objects.all(),
        widget=forms.SelectMultiple()
    )

    service_rating = forms.DecimalField(
        label=u'Serviço Adicional:',
        max_value=99999999,
        max_digits=8,
        decimal_places=2,
        localize=True,
        error_messages=error_messages,
    )

    class Meta:
        model = ServiceOrder


class PaymentForm(forms.Form):

    payment = forms.DecimalField(
        label=u'Pagamento:',
        max_value=99999999,
        max_digits=8,
        decimal_places=2,
        localize=True,
        error_messages=error_messages,
    )

    payment_date = forms.DateField(

        label=u"Data de Nascimento:",
        error_messages=date_error_messages,
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
    )

