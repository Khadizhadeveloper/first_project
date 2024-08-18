from django import template
from women.models import Category, WomanTag

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories():
    return {'categories': Category.objects.all()}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {"tags": WomanTag.objects.all()}
