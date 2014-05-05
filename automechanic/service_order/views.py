# coding:utf-8
from automechanic import templates
from django.shortcuts import render, redirect
from automechanic.service_order.forms import ServiceOrderForm, PaymentForm
from automechanic.vehicle.models import Vehicle
from automechanic.service_order.models import ServiceOrder, ServiceOrderEmployee, \
    ServiceOrderPart, AccountReceive
from automechanic.part.models import Part
from django.db.models import Sum
from django.core.urlresolvers import reverse
from automechanic.employee.models import Employee
from automechanic.messages import success_messages
from django.contrib import messages
from django.forms.models import model_to_dict


def new(request):

    return render(
                  request,
                  templates.ORDER_SERVICE_FORM, {
                      'form': ServiceOrderForm(),
                      'action': reverse('service.order.add')
                  }
    )


def load_vehicle(request):

    options_vehicle = []
    client_id = request.GET.get('client_id')

    if client_id:
        options_vehicle = Vehicle.objects.filter(client=client_id)

    return render(request, templates.ORDER_SERVICE_VEHICLE_OPTION, {'options_vehicle': options_vehicle})


def add(request):

    employees = request.POST.getlist('employees')
    parts_selecteds = request.POST.getlist('parts-selecteds')
    service_rating = request.POST.get('service_rating')
    vehicle_id = request.POST.get('vehicles')

    service_order = ServiceOrder()
    service_order.vehicle = Vehicle(id=vehicle_id)
    service_order.service_rating = service_rating
    service_order.save()

    for employee_id in employees:
        service_order_employee = ServiceOrderEmployee()
        service_order_employee.service_order = service_order
        service_order_employee.employee = Employee(id=employee_id)
        service_order_employee.save()

    for part_id in parts_selecteds:

        part = Part.objects.get(id=part_id)
        part.quantity = part.quantity - 1
        part.save()

        service_order_part = ServiceOrderPart()
        service_order_part.service_order = service_order
        service_order_part.part = part
        service_order_part.save()

    messages.add_message(request, messages.SUCCESS, u"Ordem de Serviço Gerada Com Sucesso.")

    return redirect('account.receive')


def account_receive(request):

    services_order = []

    account_receive_query = AccountReceive.objects.values('service_order').query

    for service_order in ServiceOrder.objects.exclude(id__in=account_receive_query):

        service_order_dict = model_to_dict(service_order)
        total = ServiceOrderPart.objects.filter(service_order=service_order).aggregate(Sum('part__price'))
        total = total.get('part__price__sum') + service_order.service_rating
        service_order_dict["created"] = service_order.created
        service_order_dict["client"] = service_order.vehicle.client
        service_order_dict["total"] = total
        services_order.append(service_order_dict)

    return render(
                  request,
                  templates.ORDER_SERVICE_ACCOUNT_RECEIVE, {
                      'accounts': services_order,
                  }
    )


def payment(request, service_order_id):

    service_order = ServiceOrder.objects.get(id=service_order_id)
    total = ServiceOrderPart.objects.filter(service_order=service_order).aggregate(Sum('part__price'))
    total = total.get('part__price__sum') + service_order.service_rating

    payment_form = PaymentForm(request.POST or None)

    if payment_form.is_valid():
        account_receive = AccountReceive()
        account_receive.service_order = service_order
        account_receive.value_receive = payment_form.cleaned_data.get('payment')
        account_receive.payment_date = payment_form.cleaned_data.get('payment_date')
        account_receive.maturity_date = payment_form.cleaned_data.get('payment_date')
        account_receive.save()

        messages.add_message(request, messages.SUCCESS, u"Ordem de Serviço Paga Com Sucesso.")

        return redirect('account.receive')

    return render(
                  request,
                  templates.ORDER_SERVICE_PAYMENT_FORM, {
                      'form': payment_form,
                      'total': total,
                      'service_order': service_order,
                      'action': reverse('payment', args=[service_order_id])
                  }
    )
