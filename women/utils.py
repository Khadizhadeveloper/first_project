from women.models import Category

menu = [
    {'title': "Добавить статью", 'url_name': 'woman-create'},
]


class DataMixin:
    title_page = None
    extra_context = {}
    menu = menu
    categories = Category.objects.all()
