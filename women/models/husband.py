from django.db import models


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
