# -*- coding:utf-8 -*-

from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    cpf = models.CharField(max_length=14)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'employee'
