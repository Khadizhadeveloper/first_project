from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from women.models import Women, Category, WomanTag
from .forms import AddPostForm

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add-post'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


def index(request):
    posts = Women.published.all()
    categories = Category.objects.all()
    data = {
        'title': 'Главная страница',
        'categories': categories,
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_slug):
    try:
        post = Women.objects.get(slug=post_slug)
    except Women.DoesNotExist:
        raise Http404('Page not found')

    data = {
        'title': post.title,
        'post': post,
        'menu': menu,
    }
    return render(request, 'women/post.html', context=data)


def show_category(request, category_slug):
    try:
        cat = Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
        raise Http404('Category not found')

    women = Women.published.filter(category=cat)
    categories = Category.objects.all()
    data = {
        'title': f'Категория {cat.name}',
        'categories': categories,
        'posts': women,
        'menu': menu,
    }
    return render(request, 'women/index.html', context=data)


def all_tags(request, tag_slug):
    try:
        tag = WomanTag.objects.get(slug=tag_slug)
    except WomanTag.DoesNotExist:
        raise Http404('Tag not found')

    posts = tag.women.filter(is_published=True)

    data = {
        'title': 'Главная страница',
        'posts': posts,
        'menu': menu,
    }

    return render(request, 'women/index.html', context=data)


def add_post(request):
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'women/add_post.html', {'form': form})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
