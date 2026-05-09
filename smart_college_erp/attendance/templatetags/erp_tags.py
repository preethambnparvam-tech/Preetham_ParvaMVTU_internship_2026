"""
Custom template tags used across the ERP.
Register this app's templatetags in templates with {% load erp_tags %}
"""

from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Access dict by variable key: {{ mydict|get_item:key }}"""
    if dictionary is None:
        return None
    return dictionary.get(key)


@register.filter
def dict_get(dictionary, key):
    """Alias for get_item."""
    if dictionary is None:
        return None
    return dictionary.get(key)


@register.filter
def multiply(value, arg):
    return float(value) * float(arg)


@register.filter
def subtract(value, arg):
    return float(value) - float(arg)


@register.filter
def percentage_bar_class(value):
    """Return Bootstrap color class based on percentage."""
    try:
        v = float(value)
        if v >= 75:
            return 'bg-success'
        elif v >= 60:
            return 'bg-warning'
        return 'bg-danger'
    except (ValueError, TypeError):
        return 'bg-secondary'
