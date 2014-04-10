'''
Created on 10/04/2014

@author: wsilva
'''

from django import template
register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})