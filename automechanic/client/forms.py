# -*- coding:utf-8 -*-
'''
Created on 05/04/2014

@author: William Vedroni da Silva
'''
from django import forms
from automechanic.messages import error_messages, date_error_messages, \
    cpf_messages
from automechanic.client.models import Client
from django.conf import settings
import re
from django.core.exceptions import ValidationError


class ClientForm(forms.ModelForm):

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

    nickname = forms.CharField(

        label=u"Apelido:",
        error_messages=error_messages,
        max_length=50,
        widget=forms.TextInput(attrs={'class': "input-xlarge"})
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

    def clean_cpf(self):

        try:

            digits_cpf = [10, 9, 8, 7, 6, 5, 4, 3, 2]

            cpf = re.sub('[.-]', '', self.cleaned_data.get('cpf'))

            total = 0
            for i in range(9):
                total += (int(cpf[i]) * digits_cpf[i])

            mod = (total % 11)
            first_digit = 0
            if mod >= 2:
                first_digit = (11 - mod)

            digits_cpf.insert(0, 11)

            total = 0
            for i in range(10):
                total += (int(cpf[i]) * digits_cpf[i])

            mod = (total % 11)
            second_digit = 0
            if mod >= 2:
                second_digit = (11 - mod)

            if int(cpf[9]) != first_digit:
                raise ValidationError(cpf_messages.get('invalid'))

            if int(cpf[10]) != second_digit:
                raise ValidationError(cpf_messages.get('invalid'))

            if len(set(cpf)) == 1:
                raise ValidationError(cpf_messages.get('invalid'))

            return self.cleaned_data['cpf']

        except:
            raise ValidationError(cpf_messages.get('invalid'))

    class Meta:
        model = Client


class DeleteForm(forms.Form):

    ids = forms.CharField(

        label='',
        widget=forms.HiddenInput(),
    )
