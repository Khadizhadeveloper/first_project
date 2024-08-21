from django.views.generic import DetailView
from women.models import WomanTag
from ..utils import DataMixin


class DetailTagView(DataMixin, DetailView):
    model = WomanTag
    template_name = 'women/women_list.html'
    title_page = "Главная страница"

    def get(self, request, *args, **kwargs):
        tag = WomanTag.objects.get(pk=kwargs['pk'])
        self.extra_context['object_list'] = tag.women.filter(is_published=True)
        return super(DetailTagView, self).get(request, *args, **kwargs)
