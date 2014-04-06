# -*- coding:utf-8 -*-
'''
Created on 05/04/2014

@author: William Vedroni da Silva
'''
from django import forms
from automechanic.messages import error_messages
from automechanic.client.models import Client


class ClientForm(forms.Form):

    name = forms.CharField(label=u"Nome:", error_messages=error_messages, max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))

    date_of_birth = forms.DateField(label=u"Data de Nascimento:", error_messages=error_messages, widget=forms.TextInput(attrs={'class': "form-control"}))

    nickname = forms.CharField(label=u"Apelido:", error_messages=error_messages, max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))

    cpf = forms.CharField(label=u"CPF:", error_messages=error_messages, max_length=14, widget=forms.TextInput(attrs={'class': "form-control"}))

    address = forms.CharField(label=u"Endereço:", error_messages=error_messages, max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))

    def save(self):
        data = self.cleaned_data
        client = Client()
        client.name = data.get('name', '')
        client.date_of_birth = data.get('date_of_birth', '')
        client.nickname = data.get('nickname', '')
        client.cpf = data.get('cpf', '')
        client.address = data.get('address', '')
        client.save()


class DeleteForm(forms.Form):
    ids = forms.CharField(widget=forms.HiddenInput(), label='')
