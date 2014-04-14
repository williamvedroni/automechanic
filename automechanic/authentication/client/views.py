# -*- coding:utf-8 -*-
from django.shortcuts import redirect, render
from automechanic.client.forms import ClientForm, DeleteForm
from automechanic.client.models import Client
from django.contrib import messages
from automechanic.messages import success_messages, error_messages
from django.views.decorators.http import require_http_methods
from automechanic import templates
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist


@require_http_methods(["GET"])
def list_all(request):

    context = dict()
    clients = Client.objects.all()

    context['clients'] = clients
    context['form'] = DeleteForm()
    context['action'] = reverse('client.delete')

    return render(request, templates.CLIENT_LIST, context)


@require_http_methods(["GET"])
def add(request):

    context = dict()

    context['form'] = ClientForm()
    context['action'] = reverse('client.save')

    return render(request, templates.CLIENT_FORM, context)


@require_http_methods(["POST"])
def save(request):

    context = dict()

    form = ClientForm(request.POST)

    if form.is_valid():

        form.save()
        messages.add_message(request, messages.SUCCESS, success_messages.get('success_insert'))

        return redirect('client.list')

    context['form'] = form

    return render(request, templates.CLIENT_FORM, context)


@require_http_methods(["GET"])
def edit(request, client_id):

    try:
        context = dict()
        client = Client.objects.get(pk=client_id)

        # client['date_of_birth'] = datetime.strftime(client['date_of_birth'], '%d/%m/%Y')

        context['form'] = ClientForm(instance=client)
        context['action'] = reverse('client.update', args=[client_id])

        return render(request, templates.CLIENT_FORM, context)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, error_messages.get('invalid') % 'Cliente')
        return redirect('client.list')


@require_http_methods(["POST"])
def update(request, client_id):

    try:

        client = Client.objects.get(pk=client_id)
        # client['date_of_birth'] = datetime.strftime(client['date_of_birth'], '%d/%m/%Y')

        form = ClientForm(request.POST, instance=client)

        if form.is_valid():

            form.save(request)
            messages.add_message(request, messages.SUCCESS, success_messages.get('success_edit'))

            return redirect('client.list')

        context = {'form': form}

        return render(request, templates.CLIENT_FORM, context)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, error_messages.get('invalid') % 'Cliente')
        return redirect('client.list')


@require_http_methods(["POST"])
def delete(request):

    ids = request.POST.getlist('ids')
    clients = Client.objects.filter(id__in=ids)
    clients.delete()

    messages.add_message(request, messages.SUCCESS, success_messages.get('success_remove'))

    return redirect('client.list')
