from django.contrib import admin
from django.utils.safestring import mark_safe

from women.models import Woman, Husband, WomanTag, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)
        else:
            return queryset.filter()


class HusbandAgeFilter(admin.SimpleListFilter):
    title = 'Возраст мужчин'
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return [
            ('25 - 50', 'от 25 до 50'),
            ('50 - 75', 'от 50 до 75'),
            ('75 - 100', 'от 75 до 100'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '25 - 50':
            return queryset.filter(age__gte=25, age__lte=50)
        elif self.value() == '50 - 75':
            return queryset.filter(age__gte=51, age__lte=75)
        elif self.value() == '75 - 100':
            return queryset.filter(age__gte=76, age__lte=100)
        else:
            return queryset.filter()


@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    fields = (
        'category', 'title', 'content', 'is_published', 'photo', 'show_photo', 'tags', 'husband', 'time_create',
        'time_update')
    readonly_fields = ('time_create', 'time_update', 'show_photo')
    list_display = ('id', 'title', 'is_published', 'husband', 'count_tags')
    list_display_links = ('title',)
    actions = ("set_published", "set_draft")
    # list_editable = ('is_published',)
    search_fields = ('title', 'husband__name', 'category__name')
    list_filter = ('is_published', 'category', 'tags', MarriedFilter)

    @admin.display(description="Количество тегов")
    def count_tags(self, obj: Woman):
        return f"Count tags = {obj.tags.count()}"

    @admin.display(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        queryset.update(is_published=Woman.Status.PUBLISHED)

    @admin.display(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        queryset.update(is_published=Woman.Status.DRAFT)

    @admin.display(description="Изображение")
    def show_photo(self, women: Woman):
        if women.photo:
            return mark_safe(f'<img src="women.photo.url" width=200>')
        return None


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    fields = ('name', 'age')
    list_display = ('id', 'name', 'age')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = (HusbandAgeFilter,)


@admin.register(WomanTag)
class WomanTagAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
