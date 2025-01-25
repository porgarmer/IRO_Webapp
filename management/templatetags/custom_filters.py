from django import template

register = template.Library()

@register.filter
def default_image(value, default_image_url):
    return value.url if value else default_image_url