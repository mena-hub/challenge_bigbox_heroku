from django import template
from bigbox.models import Box

register = template.Library()

@register.simple_tag
def get_box_list():
    boxes = Box.objects.all()
    return boxes