from django.db import models


class LinkButton(models.Model):
    """Модель кнопки со ссылкой"""

    title = models.CharField(verbose_name='Title', max_length=255)  # Название кнопки
    link = models.TextField(verbose_name='Link')  # Ссылка, зашиваемая в кнопку

    class Meta:
        verbose_name = 'LinkButton'
        verbose_name_plural = 'LinkButtons'

    def __str__(self):
        return self.title


class Payment(models.Model):
    """Модель кнопки оплаты"""

    title = models.CharField(verbose_name='Title', max_length=255)  # Название кнопки

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.title
