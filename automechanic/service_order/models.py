# coding:utf-8
from django.db import models
from automechanic.authentication.client.models import Client
from automechanic.employee.models import Employee


class ServiceOrder(models.Model):

    client = models.OneToOneField(Client)
    employees = models.ForeignKey(Employee)
