from django.contrib.auth.mixins import LoginRequiredMixin

from women.models import Woman
from ..forms import AddPostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from ..utils import DataMixin


class WomanListView(ListView):
    model = Woman
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = None
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Woman.published.all()


class WomanDetailView(LoginRequiredMixin, DataMixin, DetailView):
    model = Woman
    title_page = 'Детальная страница',


class WomanUpdateView(LoginRequiredMixin, DataMixin, UpdateView):
    model = Woman
    form_class = AddPostForm
    title_page = 'Изменить данный пост'


class WomanCreateView(LoginRequiredMixin, CreateView):
    model = Woman
    form_class = AddPostForm
    template_name = "women/add_post.html"

    def form_valid(self, form):
        woman = form.save(commit=False)
        woman.author = self.request.user
        return super().form_valid(form)
