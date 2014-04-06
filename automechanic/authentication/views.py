# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def login(request):

    template = 'login.html'

    return render_to_response(template, context_instance=RequestContext(request))
