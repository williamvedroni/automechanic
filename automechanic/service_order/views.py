# coding:utf-8
from automechanic import templates
from django.shortcuts import render
from automechanic.service_order.forms import ServiceOrderForm


def new(request):

    return render(request, templates.ORDER_SERVICE_FORM, {'form': ServiceOrderForm()})
