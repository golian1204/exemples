from django.contrib.auth.models import User
from django.db import models

import uuid


class SubsList(models.Model):
    """Подписной лист"""

    # Todo name сделать уникальным, когда будет проверка на фронте на уникальность
    user = models.ForeignKey(User, verbose_name='Client', on_delete=models.CASCADE)  # клиент, под которым создан подписной лист
    name = models.CharField(verbose_name='Title', max_length=40)  # название подписного листа
    description = models.TextField(verbose_name='Description', null=True, blank=True, max_length=80)  # описание подписного лист
    uuid = models.UUIDField(verbose_name='UUID', unique=True, default=uuid.uuid4)  # uuid подписного листа
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=True)  # дата создания подписного листа
    deleted = models.NullBooleanField(verbose_name='Deleted')  # True-удален, т.е. перенесен в архив, False/null - действующий

    class Meta:
        verbose_name = 'Subscription list'
        verbose_name_plural = 'Subscription lists'

    def __str__(self):
        return self.name
