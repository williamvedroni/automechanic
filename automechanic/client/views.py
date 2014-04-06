# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from automechanic.client.forms import ClientForm
from automechanic.client.models import Client
from django.contrib import messages
from automechanic.messages import success_messages


def list_all(request):

    clients = Client.objects.all()
    context = {'clients': clients}

    return render_to_response('client/list.html', context, context_instance=RequestContext(request))


def add(request):

    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, success_messages.get("success_insert"))
        return redirect('client.list')

    context = {'form': form}

    return render_to_response('client/form.html', context, context_instance=RequestContext(request))
