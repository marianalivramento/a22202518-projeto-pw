from django import template

register = template.Library()

@register.filter
def praias_ordenadas(regiao):
    return regiao.praia.all().order_by('nome')