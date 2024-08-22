from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from women.models import Women, Category, WomanTag
from .forms import AddPostForm
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add-post'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


class ShowCategoryView(DetailView):
    model = Category
    template_name = 'women/woman_list.html'

    extra_context = {
        'title': f'Категория',
        'categories': Category.objects.all(),
        'menu': menu,
    }

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=kwargs['pk'])
        self.extra_context['object_list'] = Women.published.filter(category=category)
        return super(ShowCategoryView, self).get(request, *args, **kwargs)




def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
