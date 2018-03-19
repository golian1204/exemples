from django.db import models
from mess.models import mess
from subscriptions.models.subscribers import Subscribers


class YesNoStatistic(models.Model):
    """Статистика ответов Да-Нет"""

    mess = models.ForeignKey(mess.Mess, verbose_name='Mess', on_delete=models.CASCADE)  # идентификатор Mess, содержащего кнопки Да/Нет
    subscriber = models.ForeignKey(Subscribers, verbose_name='Subscriber', on_delete=models.CASCADE)  # идентификатор подписчика
    yes = models.NullBooleanField(verbose_name='Yes')  # True-ответил Да, False-ответил нет, null-не ответил

    class Meta:
        verbose_name = 'YesNoStatistic'
        verbose_name_plural = 'YesNoStatistics'
        unique_together = ('mess', 'subscriber')

    def __str__(self):
        return str(self.pk)
