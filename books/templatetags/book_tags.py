from django import template

# custom filter tags define here.
register = template.Library()


# lowercase
@register.filter
def to_lowercase(value):
    return value.lower()
