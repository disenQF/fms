from django.template.defaultfilters import register


@register.filter(is_safe=True)
def dot_info(value):
    if len(value)>10:
        return value[:10]+'...'

    return value