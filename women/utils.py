"""
p.count # число элементов в списке
p.num_pages # число страниц (10:3 = 4 – округление до большего)
p.page_range # итератор для перебора номеров страниц
p1 = p.page(1) # получение первой страницы
p1.object_list # список элементов текущей страницы
p1.has_next() # имеется ли следующая страница
p1.has_previous() # имеется ли предыдущая страница
p1.has_other_pages() # имеются ли вообще страницы
p1.next_page_number() # номер следующей страницы
p1.previous_page_number() # номер предыдущей страницы
"""
menu = [
    # {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'women:woman-create'},
    # {'title': "Обратная связь", 'url_name': 'contact'},
    # {'title': "Войти", 'url_name': 'login'}
]


class DataMixin:
    title_page = None
    extra_context = {}

    def get_mixin_context(self, **kwargs):
        context = kwargs
        if self.title_page:
            context['title'] = self.title_page

        context['menu'] = menu
        return context
