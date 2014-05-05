# -*- coding:utf-8 -*-

from django.db import models


class Part(models.Model):

    description = models.CharField(
        max_length=200
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    quantity = models.IntegerField(
    )

    class Meta:
        db_table = 'part'

    def __unicode__(self):
        return self.description
