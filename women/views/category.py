from django.views.generic import DetailView
from women.models import Category, Women
from ..utils import DataMixin


class ShowCategoryView(DataMixin, DetailView):
    model = Category
    title_page = 'Категория'
    template_name = 'women/women_list.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=kwargs['pk'])
        self.extra_context['object_list'] = Women.published.filter(category=category)
        return super(ShowCategoryView, self).get(request, *args, **kwargs)
