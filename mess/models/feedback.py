from django.db import models


class Valuation(models.Model):
    """Модель оценки"""

    scale = models.PositiveSmallIntegerField(verbose_name='Scale')  # шкала\бальность оценки (3, 5 или 10)
    icon = models.TextField(verbose_name='Icon')  # css класс в виде строки, например 'icon-done icon-succesful'

    class Meta:
        verbose_name = 'Valuation'
        verbose_name_plural = 'Valuations'

    def __str__(self):
        return self.scale
