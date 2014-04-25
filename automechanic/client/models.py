# -*- coding:utf-8 -*-

from django.db import models


class Client(models.Model):

    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    nickname = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = 'client'

    def __unicode__(self):
        return self.name
