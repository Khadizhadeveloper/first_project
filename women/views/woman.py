from women.models import Woman
from ..forms import AddPostForm
from django.views.generic import ListView, DetailView, CreateView
from ..utils import DataMixin


class WomanListView(ListView):
    model = Woman
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = None
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Woman.published.all()


class WomanDetailView(DataMixin, DetailView):
    model = Woman
    title_page = 'Детальная страница',


class WomanCreateView(CreateView):
    model = Woman
    form_class = AddPostForm
    template_name = "women/add_post.html"
