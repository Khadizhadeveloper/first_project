from django.db import models
from django.shortcuts import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class WomanTag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
    )

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

    def __str__(self):
        return self.name


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    # def get_absolute_url(self):
    #     return reverse()

    def __str__(self):
        return self.name


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
    )
    content = models.TextField(blank=True)
    is_published = models.BooleanField(
        choices=Status.choices,
        default=Status.DRAFT,
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.PROTECT,
        related_name='women',
        null=True,
    )
    husband = models.OneToOneField(
        Husband,
        on_delete=models.SET_NULL,
        related_name='wife',
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        WomanTag,
        related_name='women',
    )

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-time_create',)
        indexes = [models.Index(fields=['-time_create'])]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title
