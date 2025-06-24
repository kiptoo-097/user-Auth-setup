from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    attrs = {"class": css_class, "placeholder": field.label}
    if field.name in ["phone_number", "username"]:
        attrs["inputmode"] = "numeric"
    return field.as_widget(attrs=attrs)
