# -*- coding:utf-8 -*-
'''
Created on 05/04/2014

@author: William Vedroni da Silva
'''
from django import forms
from automechanic.messages import error_messages, date_error_messages, \
    success_messages
from automechanic.client.models import Client
from django.contrib import messages


class ClientForm(forms.Form):

    id = forms.CharField(widget=forms.HiddenInput(), label='', required=False)
    name = forms.CharField(label=u"Nome:", error_messages=error_messages, max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))
    date_of_birth = forms.DateField(label=u"Data de Nascimento:", error_messages=date_error_messages, widget=forms.TextInput(attrs={'class': "form-control"}))
    nickname = forms.CharField(label=u"Apelido:", error_messages=error_messages, max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
    cpf = forms.CharField(label=u"CPF:", error_messages=error_messages, max_length=14, widget=forms.TextInput(attrs={'class': "form-control"}))
    address = forms.CharField(label=u"Endereço:", error_messages=error_messages, max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))

    def save(self, request):
        data = self.cleaned_data
        client = Client()

        if data.get('id') is not None:
            client.id = data.get('id', '')
            messages.add_message(request, messages.SUCCESS, success_messages.get("success_edit"))
        else:
            messages.add_message(request, messages.SUCCESS, success_messages.get("success_insert"))

        client.name = data.get('name', '')
        client.date_of_birth = data.get('date_of_birth', '')
        client.nickname = data.get('nickname', '')
        client.cpf = data.get('cpf', '')
        client.address = data.get('address', '')
        client.save()


class DeleteForm(forms.Form):
    ids = forms.CharField(widget=forms.HiddenInput(), label='')
