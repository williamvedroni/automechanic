# -*- coding:utf-8 -*-

from django.db import models
from automechanic.client.models import Client


class Vehicle(models.Model):

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        db_column='client_id'
    )

    license_plate = models.CharField(
        max_length=8
    )

    vehicle_model = models.CharField(
        max_length=50
    )

    fabricator = models.CharField(

        max_length=50
    )

    color = models.CharField(

        max_length=15
    )

    fabrication_year = models.IntegerField(

    )

    class Meta:
        db_table = 'vehicle'

    def __unicode__(self):
        return self.vehicle_model + ' - ' +self.license_plate