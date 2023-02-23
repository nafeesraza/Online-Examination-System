from atexit import register
from django import template
import datetime
register=template.Library()

@register.simple_tag(name="get_date")
def get_date():
    x=datetime.datetime.now()
    return x;
@register.filter
def quotes(value):
    s='"'+str(value)+'"'
    return s