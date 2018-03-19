from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models


class Profiles(models.Model):
    """Профиль пользователя системы"""

    ROLE_CHOICES = (
        (1, 'Client'),
        (2, 'Employee of the client'),
        (3, 'Employee'),
        (4, 'Service'),
        (5, 'Bot'),
    )
    user = models.OneToOneField(User, verbose_name='Client', on_delete=models.CASCADE)  # зареестрированный пользоватлеь системы
    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name='User Type', default=ROLE_CHOICES[0][0])  # роль рользователя (для определения прав доступа)
    hash = models.CharField(verbose_name='User hash', max_length=200, null=True, blank=True)  # hash пользователя (для безопасной передачи данных)
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=True)  # дата регистрации пользователя

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profiles.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profiles.save()
