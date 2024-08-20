import uuid
from django.db import models
from django.shortcuts import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class WomanTag(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
    )

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Husband(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
    )
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")

    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        verbose_name = 'Мужи Известных женщин'
        verbose_name_plural = 'Мужи Известных женщин'

    def __str__(self):
        return self.name


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
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

    def save(self, *args, **kwargs):
        self.slug = self.slug + "_" + str(uuid.uuid4())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
