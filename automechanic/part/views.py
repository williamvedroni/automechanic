# -*- coding:utf-8 -*-
from django.shortcuts import redirect, render
from django.contrib import messages
from automechanic.messages import success_messages, error_messages
from django.views.decorators.http import require_http_methods
from automechanic import templates
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from automechanic.part.models import Part
from automechanic.part.forms import PartForm
from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(["GET"])
def list_all(request):

    context = dict()
    parts = Part.objects.all()

    context['parts'] = parts
    context['action'] = reverse('part.delete')

    return render(request, templates.PART_LIST, context)


@login_required
@require_http_methods(["GET"])
def add(request):

    context = dict()

    context['form'] = PartForm()
    context['action'] = reverse('part.save')

    return render(request, templates.PART_FORM, context)


@login_required
@require_http_methods(["POST"])
def save(request):

    context = dict()

    form = PartForm(request.POST)

    if form.is_valid():

        form.save()
        messages.add_message(request, messages.SUCCESS, success_messages.get('success_insert'))

        return redirect('part.list')

    context['form'] = form

    return render(request, templates.PART_FORM, context)


@login_required
@require_http_methods(["GET"])
def edit(request, part_id):

    try:
        context = dict()
        part = Part.objects.get(pk=part_id)

        context['form'] = PartForm(instance=part)
        context['action'] = reverse('part.update', args=[part_id])

        return render(request, templates.PART_FORM, context)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, error_messages.get('invalid') % u'Peça')
        return redirect('part.list')


@login_required
@require_http_methods(["POST"])
def update(request, part_id):

    try:
        context = dict()
        part = Part.objects.get(pk=part_id)
        form = PartForm(request.POST, instance=part)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, success_messages.get('success_edit'))

            return redirect('part.list')

        context['form'] = form

        return render(request, templates.PART_FORM, context)

    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, error_messages.get('invalid') % u'Peça')
        return redirect('part.list')


@login_required
@require_http_methods(["POST"])
def delete(request):

    ids = request.POST.getlist('ids')
    parts = Part.objects.filter(id__in=ids)
    parts.delete()

    messages.add_message(request, messages.SUCCESS, success_messages.get('success_remove'))

    return redirect('part.list')
