from django.db import models
from django.urls import reverse


class WomanTag(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя",
    )

    def get_absolute_url(self):
        return reverse('women:woman-tag-detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
