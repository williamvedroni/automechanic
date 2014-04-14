# -*- coding:utf-8 -*-
'''
Created on 05/04/2014

@author: William Vedroni da Silva
'''
from django import forms
from automechanic.messages import error_messages, date_error_messages, \
    cpf_messages
from automechanic.employee.models import Employee
from django.core.exceptions import ValidationError
from automechanic.validators import validator_cpf


class EmployeeForm(forms.ModelForm):

    name = forms.CharField(

        label=u"Nome:",
        error_messages=error_messages,
        max_length=200,
        widget=forms.TextInput(attrs={'class': "input-xxlarge"})
    )

    date_of_birth = forms.DateField(

        label=u"Data de Nascimento:",
        error_messages=date_error_messages,
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
    )

    cpf = forms.CharField(

        label=u"CPF:",
        error_messages=error_messages,
        max_length=14,
    )
    address = forms.CharField(

        label=u"Endereço:",
        error_messages=error_messages,
        max_length=200,
        widget=forms.TextInput(attrs={'class': "input-xxlarge"})
    )

    phone_number = forms.CharField(

        label=u"Telefone:",
        error_messages=error_messages,
        max_length=13,
    )

    def clean_cpf(self):

        try:
            validator_cpf(self.cleaned_data.get('cpf'))

            return self.cleaned_data.get('cpf')

        except ValidationError:
            raise ValidationError(cpf_messages.get('invalid'))

    class Meta:
        model = Employee
