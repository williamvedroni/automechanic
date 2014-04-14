# -*- coding:utf-8 -*-
'''
Created on 05/04/2014

@author: William Vedroni da Silva
'''
from django import forms
from automechanic.messages import error_messages
from django.core.exceptions import ValidationError
from automechanic.part.models import Part


class PartForm(forms.ModelForm):

    description = forms.CharField(
        label=u'Descrição:',
        max_length=200,
        error_messages=error_messages,
        widget=forms.TextInput(attrs={'class': "input-xxlarge"})
    )

    price = forms.DecimalField(
        label=u'Preço:',
        max_value=99999999,
        max_digits=8,
        decimal_places=2,
        localize=True,
        error_messages=error_messages,
    )

    quantity = forms.IntegerField(
        label=u'Quantidade:',
        max_value=99999999,
        error_messages=error_messages,
    )

    class Meta:
        model = Part
