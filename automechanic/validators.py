# -*- coding:utf-8 -*-
'''
Created on 10/04/2014

@author: wsilva
'''
from django.core.exceptions import ValidationError
import re


def validator_cpf(value):

    try:

        digits_cpf = [10, 9, 8, 7, 6, 5, 4, 3, 2]

        cpf = re.sub('[.-]', '', value)

        total = 0
        for i in range(9):
            total += (int(cpf[i]) * digits_cpf[i])

        mod = (total % 11)
        first_digit = 0
        if mod >= 2:
            first_digit = (11 - mod)

        digits_cpf.insert(0, 11)

        total = 0
        for i in range(10):
            total += (int(cpf[i]) * digits_cpf[i])

        mod = (total % 11)
        second_digit = 0
        if mod >= 2:
            second_digit = (11 - mod)

        if int(cpf[9]) != first_digit:
            raise ValidationError(u'')

        if int(cpf[10]) != second_digit:
            raise ValidationError(u'')

        if len(set(cpf)) == 1:
            raise ValidationError(u'')

    except:

        raise ValidationError(u'')
