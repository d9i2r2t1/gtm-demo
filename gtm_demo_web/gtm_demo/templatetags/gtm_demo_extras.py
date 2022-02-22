from django import template

from gtm_demo.models import DemoLanding

register = template.Library()


@register.simple_tag
def get_landings_count():
    return DemoLanding.objects.count()


@register.filter(name="get")
def get(dictionary, key):
    return dictionary.get(key, None)
