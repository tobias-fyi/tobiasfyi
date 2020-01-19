"""
Navigator :: Template Tags
"""

from django import template

from ..models import Nav

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Nav.objects.get(slug=slug)
