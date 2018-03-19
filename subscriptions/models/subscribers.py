from django.db import models
from subscriptions.models.subs_list import SubsList
from auth_client.models.messengers import Messengers
from django.contrib.auth.models import User


class Subscribers(models.Model):
    """Модель подписчика"""

    TYPE_CHOICES = Messengers.TYPE_CHOICES

    user = models.ForeignKey(User, verbose_name='Client', on_delete=models.CASCADE)  # клиент, под которым создан подписчик
    bot_id = models.CharField(verbose_name='User ID in bot', max_length=200)  # идентификатор подписчика в мессенджере
    name_messenger = models.CharField(verbose_name='Messenger', choices=TYPE_CHOICES, max_length=10)  # тип мессенджера
    username = models.CharField(verbose_name='Username', max_length=200)  # ник подписчика в мессенджере
    first_name = models.CharField(verbose_name='First name', max_length=200, null=True, blank=True)  # имя подписчика в месенджере
    last_name = models.CharField(verbose_name='Last name', max_length=200, null=True, blank=True)  # фамилия подписчика в месенджере
    created_date = models.DateTimeField(verbose_name='Created date', auto_now_add=True)  # дата добавления подписчика
    subscribed = models.NullBooleanField(verbose_name='Subscribed')  # True-подписан на бота, False/null-отписался
    chat_bot = models.CharField(verbose_name='Bot ID in messenger', max_length=200)  # идентификатор бота в мессенджере
    phone = models.CharField(verbose_name='Phone', max_length=20, null=True, blank=True)  # телефон подписчика

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
        unique_together = ('bot_id', 'chat_bot')

    def __str__(self):
        return self.username


class Subscriptions(models.Model):
    """Подписки. Привязка подписчиков к подписным листам"""

    subs_list = models.ForeignKey(SubsList, verbose_name='Subscription list', on_delete=models.CASCADE)  # идентификатор подписного листа
    subscriber = models.ForeignKey(Subscribers, verbose_name='Subscriber', on_delete=models.CASCADE)  # идентификатор подписчика
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=True)  # дата добавления подписчика в подписной лист
    deleted = models.NullBooleanField(verbose_name='Deleted')  # True-удален из подписного листа, False/null-в подписном листе

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        unique_together = ('subs_list', 'subscriber')

    def __str__(self):
        return str(self.pk)
