# -*- coding:utf-8 -*-
'''
Created on 05/04/2014

@author: William Vedroni da Silva
'''
from django import forms
from automechanic.messages import error_messages
from django.core.exceptions import ValidationError
from automechanic.vehicle.models import Vehicle


class VehicleForm(forms.ModelForm):

    license_plate = forms.CharField(

        label=u"Placa:",
        error_messages=error_messages,
        max_length=8,
    )

    vehicle_model = forms.CharField(

        label=u"Modelo:",
        error_messages=error_messages,
        max_length=50,
        widget=forms.TextInput(attrs={'class': "input-xlarge"})
    )

    fabricator = forms.CharField(

        label=u"Fabricante:",
        error_messages=error_messages,
        max_length=50,
        widget=forms.TextInput(attrs={'class': "input-xlarge"})
    )

    color = forms.CharField(

        label=u"Cor:",
        error_messages=error_messages,
        max_length=15,
    )
    fabrication_year = forms.CharField(

        label=u"Ano de Fabricação:",
        error_messages=error_messages,
        max_length=4,
    )

    class Meta:
        model = Vehicle
        widgets = {
            'client': forms.HiddenInput()
        }
