# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from automechanic.client.forms import ClientForm, DeleteForm
from automechanic.client.models import Client
from django.contrib import messages
from automechanic.messages import success_messages
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from datetime import date, datetime


def list_all(request):

    clients = Client.objects.all()
    context = {'clients': clients, 'form': DeleteForm()}

    return render_to_response('client/list.html', context, context_instance=RequestContext(request))


def add(request):

    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save(request)
        return redirect('client.list')

    context = {'form': form}

    return render_to_response('client/form.html', context, context_instance=RequestContext(request))


@require_http_methods(["GET"])
def edit(request, client_id):

    try:

        client = model_to_dict(Client.objects.get(pk=client_id))
        client['date_of_birth'] = datetime.strftime(client['date_of_birth'], '%d/%m/%Y')

        form = ClientForm(client)

        context = {'form': form}
    except Exception as exception:
        print str(exception)

    return render_to_response('client/form.html', context, context_instance=RequestContext(request))


@require_http_methods(["POST"])
def update(request, client_id):

    try:

        client = model_to_dict(Client.objects.get(pk=client_id))
        client['date_of_birth'] = datetime.strftime(client['date_of_birth'], '%d/%m/%Y')

        form = ClientForm(client)

        context = {'form': form}
    except Exception as exception:
        print str(exception)

    return render_to_response('client/form.html', context, context_instance=RequestContext(request))
