from django.shortcuts import render, redirect
from women.models import Women
from ..forms import AddPostForm
from django.views import View
from django.views.generic import ListView, DetailView
from ..utils import DataMixin


class WomenListView(DataMixin, ListView):
    model = Women
    title_page = 'Главная страница'

    def get_queryset(self):
        return Women.published.all()


class WomanDetailView(DataMixin, DetailView):
    model = Women
    title_page = 'Главная страница',


class WomanCreateView(View):
    def get(self, request):
        form = AddPostForm()
        return render(request, 'women/add_post.html', {'form': form})

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('woman-create')
        return render(request, 'women/add_post.html', {'form': form})