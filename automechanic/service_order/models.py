# coding:utf-8
from django.db import models
from automechanic.employee.models import Employee
from automechanic.vehicle.models import Vehicle
from automechanic.part.models import Part


class ServiceOrder(models.Model):

    vehicle = models.ForeignKey(Vehicle)

    created = models.DateTimeField(auto_now_add=True)

    service_rating = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )


class ServiceOrderEmployee(models.Model):

    service_order = models.ForeignKey(ServiceOrder)
    employee = models.ForeignKey(Employee)


class ServiceOrderPart(models.Model):

    service_order = models.ForeignKey(ServiceOrder)
    part = models.ForeignKey(Part)


class AccountReceive(models.Model):

    service_order = models.ForeignKey(ServiceOrder)

    value_receive = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    payment_date = models.DateTimeField()

    maturity_date = models.DateTimeField()
