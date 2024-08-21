from django.db import models
from django.shortcuts import reverse


class WomanTag(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя",
    )

    def get_absolute_url(self):
        return reverse('woman-tag-detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
