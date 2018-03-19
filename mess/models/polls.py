from django.db import models
from django.contrib.auth.models import User


class Interview(models.Model):
    """Модель опроса"""

    # Todo title сделать уникальным, когда будет проверка на фронте на уникальность
    user = models.ForeignKey(User, verbose_name='Client', on_delete=models.CASCADE)  # клиент, под которым создан Mess
    title = models.CharField(verbose_name='Title', max_length=255)  # название опроса
    created_date = models.DateTimeField(verbose_name='Date', auto_now=True)  # дата создания

    class Meta:
        verbose_name = 'Interview'
        verbose_name_plural = 'Interviews'

    def __str__(self):
        return self.title


class Answers(models.Model):
    """Модель ответа для опроса"""

    # Для опроса максимум может быть 10 ответов
    ORDER_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
    )

    interview = models.ForeignKey(Interview, verbose_name='Interview', on_delete=models.CASCADE)  # идентификатор интервью
    title = models.TextField(verbose_name='Text')  # текст ответа
    order = models.IntegerField(choices=ORDER_CHOICES, verbose_name='Order')  # номер ответа в списке

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        unique_together = ('interview', 'order')

    def __str__(self):
        return self.title
