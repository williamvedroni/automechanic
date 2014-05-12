# -*- coding:utf-8 -*-
from django.shortcuts import redirect, render
from automechanic.employee.forms import EmployeeForm
from automechanic.employee.models import Employee
from django.contrib import messages
from automechanic.messages import success_messages, error_messages
from django.views.decorators.http import require_http_methods
from automechanic import templates
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(["GET"])
def list_all(request):

    context = dict()
    employees = Employee.objects.all()

    context['employees'] = employees
    context['action'] = reverse('employee.delete')

    return render(request, templates.EMPLOYEE_LIST, context)


@login_required
@require_http_methods(["GET"])
def add(request):

    context = dict()

    context['form'] = EmployeeForm()
    context['action'] = reverse('employee.save')

    return render(request, templates.EMPLOYEE_FORM, context)


@login_required
@require_http_methods(["POST"])
def save(request):

    context = dict()

    form = EmployeeForm(request.POST)

    if form.is_valid():

        form.save()
        messages.add_message(request, messages.SUCCESS, success_messages.get('success_insert'))

        return redirect('employee.list')

    context['form'] = form

    return render(request, templates.EMPLOYEE_FORM, context)


@login_required
@require_http_methods(["GET"])
def edit(request, employee_id):

    try:
        context = dict()
        employee = Employee.objects.get(pk=employee_id)

        context['form'] = EmployeeForm(instance=employee)
        context['action'] = reverse('employee.update', args=[employee_id])

        return render(request, templates.EMPLOYEE_FORM, context)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, error_messages.get('invalid') % u'Funciońario')
        return redirect('employee.list')


@login_required
@require_http_methods(["POST"])
def update(request, employee_id):

    try:

        employee = Employee.objects.get(pk=employee_id)

        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():

            form.save(request)
            messages.add_message(request, messages.SUCCESS, success_messages.get('success_edit'))

            return redirect('employee.list')

        context = {'form': form}

        return render(request, templates.EMPLOYEE_FORM, context)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, error_messages.get('invalid') % u'Funcionário')
        return redirect('employee.list')


@login_required
@require_http_methods(["POST"])
def delete(request):

    ids = request.POST.getlist('ids')
    employees = Employee.objects.filter(id__in=ids)
    employees.delete()

    messages.add_message(request, messages.SUCCESS, success_messages.get('success_remove'))

    return redirect('employee.list')
