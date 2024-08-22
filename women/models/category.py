from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
    )

    def get_absolute_url(self):
        return reverse("women:woman-category-detail", kwargs={"pk": self.id})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
