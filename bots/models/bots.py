from django.contrib.auth.models import User
from django.db import models
from auth_client.models.messengers import Messengers


class Bots(models.Model):
    """Боты клиентов"""

    TYPE_CHOICES = Messengers.TYPE_CHOICES

    user = models.ForeignKey(User, verbose_name='Client')  # идентификатор клиента
    name = models.CharField(verbose_name='Name bot', max_length=100)  # имя бота клиента
    type_messenger = models.CharField('Type messenger', choices=TYPE_CHOICES, max_length=10)  # тип мессенджера
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=True)  # дата создания бота

    class Meta:
        verbose_name = 'Bot'
        verbose_name_plural = 'Bots'

    def __str__(self):
        return self.name


class TokensTelegram(models.Model):
    """Данные ботов в Telegram"""

    bot = models.OneToOneField(Bots, verbose_name='Bot')  # идентификатор бота
    token = models.CharField(verbose_name='Token', max_length=250)  # токен бота
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=True)  # дата обновленния данных

    class Meta:
        verbose_name = 'Token Telegram bot'
        verbose_name_plural = 'Tokens Telegram bots'

    def __str__(self):
        return self.bot.name


class TokensViber(models.Model):
    """Данные ботов в Viber"""

    bot = models.OneToOneField(Bots, verbose_name='Bot')  # идентификатор бота
    token = models.CharField(verbose_name='Token', max_length=250)  # токен бота
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=True)  # дата обновленния данных

    class Meta:
        verbose_name = 'Token Viber bot'
        verbose_name_plural = 'Tokens Viber bots'

    def __str__(self):
        return self.bot.name


class TokensFacebook(models.Model):
    """Данные ботов в Facebook"""

    bot = models.OneToOneField(Bots, verbose_name='Bot')  # идентификатор бота
    token = models.CharField(verbose_name='Token', max_length=250)  # токен бота
    verify_token = models.CharField(verbose_name='Verify token', max_length=250)  # маркер подтверждения (строка, добавляемая в каждый запрос на подтверждение)
    id_page = models.CharField(verbose_name='ID page', max_length=250)  # ид приложения бота на Facebook for developers
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=True)  # дата обновления данных

    class Meta:
        verbose_name = 'Token Facebook bot'
        verbose_name_plural = 'Tokens Facebook bots'

    def __str__(self):
        return self.bot.name
