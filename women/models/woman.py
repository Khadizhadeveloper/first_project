from django.contrib.auth import get_user_model
from django.db import models
from .husband import Husband
from .woman_tag import WomanTag
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Woman.Status.PUBLISHED)


class Woman(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
    )
    content = models.TextField(
        blank=True,
        verbose_name='Текст статьи'
    )
    is_published = models.BooleanField(
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='Статус'
    )
    photo = models.ImageField(
        upload_to=f'women/{title}/',
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name='women',
        verbose_name='Автор',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.PROTECT,
        related_name='women',
        null=True,
        verbose_name='Категория'
    )
    husband = models.OneToOneField(
        Husband,
        on_delete=models.SET_NULL,
        related_name='wife',
        null=True,
        blank=True,
        verbose_name='Муж'
    )
    tags = models.ManyToManyField(
        WomanTag,
        related_name='women',
        verbose_name='Теги'
    )

    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания',
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Время изменения',
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-time_create',)
        indexes = [models.Index(fields=['-time_create'])]
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('women:woman-detail', kwargs={'pk': self.id})
