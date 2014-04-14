# -*- coding:utf-8 -*-
from django.shortcuts import redirect, render
from django.contrib import messages
from automechanic.messages import success_messages, error_messages
from django.views.decorators.http import require_http_methods
from automechanic import templates
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from automechanic.vehicle.models import Vehicle
from automechanic.vehicle.forms import VehicleForm


@require_http_methods(["GET"])
def list_all(request, client_id):

    context = dict()
    vehicles = Vehicle.objects.filter(client=client_id)

    context['client_id'] = client_id
    context['vehicles'] = vehicles
    context['action'] = reverse('vehicle.delete', args=[client_id])

    return render(request, templates.VEHICLE_LIST, context)


@require_http_methods(["GET"])
def add(request, client_id):

    context = dict()

    context['client_id'] = client_id
    context['form'] = VehicleForm(initial={'client': client_id})
    context['action'] = reverse('vehicle.save', args=[client_id])

    return render(request, templates.VEHICLE_FORM, context)


@require_http_methods(["POST"])
def save(request, client_id):

    context = dict()

    form = VehicleForm(request.POST)

    if form.is_valid():

        form.save()
        messages.add_message(request, messages.SUCCESS, success_messages.get('success_insert'))

        return redirect('vehicle.list', client_id)

    context['form'] = form
    context['client_id'] = client_id

    return render(request, templates.VEHICLE_FORM, context)


@require_http_methods(["GET"])
def edit(request, vehicle_id):

    try:
        context = dict()
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        client_id = vehicle.client.id

        context['form'] = VehicleForm(instance=vehicle)
        context['action'] = reverse('vehicle.update', args=[vehicle_id])
        context['client_id'] = client_id

        return render(request, templates.VEHICLE_FORM, context)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, error_messages.get('invalid') % u'Veículo')
        return redirect('vehicle.list', client_id)


@require_http_methods(["POST"])
def update(request, vehicle_id):

    try:
        context = dict()
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        client_id = vehicle.client.id

        form = VehicleForm(request.POST, instance=vehicle)

        if form.is_valid():

            form.save(request)
            messages.add_message(request, messages.SUCCESS, success_messages.get('success_edit'))

            return redirect('vehicle.list', client_id)

        context['form'] = form

        return render(request, templates.VEHICLE_FORM, context)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, error_messages.get('invalid') % u'Veículo')
        return redirect('vehicle.list', client_id)


@require_http_methods(["POST"])
def delete(request, client_id):

    ids = request.POST.getlist('ids')
    vehicles = Vehicle.objects.filter(client=client_id, id__in=ids)
    vehicles.delete()

    messages.add_message(request, messages.SUCCESS, success_messages.get('success_remove'))

    return redirect('vehicle.list', client_id)
# Create your views here.
