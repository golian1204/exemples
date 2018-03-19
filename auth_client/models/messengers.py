from django.contrib.auth.models import User
from django.db import models


class Messengers(models.Model):
    """Messenger авторизации клиента через ботов"""

    TYPE_CHOICES = (
        ('telegram', 'Telegram'),
        ('fb', 'Facebook'),
        ('viber', 'Viber'),
    )

    user = models.OneToOneField(User, verbose_name='Client', on_delete=models.CASCADE)  # идентификатор клиента
    user_id_bot = models.CharField(verbose_name='User ID in bot', max_length=200)  # идентификатор клиента в боте
    name_messenger = models.CharField(verbose_name='Messenger', choices=TYPE_CHOICES, max_length=10)  # мессенджер авторизации клиента
    bot_id = models.CharField(verbose_name='ID bot', max_length=200)  # идентификатор бота в мессенджере
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=True)  # дата авторизации клиента

    class Meta:
        verbose_name = 'User authorization messenger'
        verbose_name_plural = 'User authorization messengers'

    def __str__(self):
        return self.name_messenger
