from django.contrib.auth.models import User
from django.db import models
from mess.models.attachments import Images
from subscriptions.models.subs_list import SubsList


class SubsBlank(models.Model):
    """Форма подписки"""

    # Todo title сделать уникальным, когда будет проверка на фронте на уникальность
    title = models.CharField(verbose_name='Title', max_length=40)  # название
    description = models.TextField(verbose_name='Description', null=True, blank=True, max_length=80)  # описание
    offer = models.CharField(verbose_name='Offer', max_length=45)  # уникальное торговое предложение
    call_to_action = models.CharField(verbose_name='CallToAction', max_length=35)  # призыв к действию
    telegram = models.NullBooleanField(verbose_name='Telegram')  # наличие кнопки подписки через Telegram
    facebook = models.NullBooleanField(verbose_name='Facebook')  # наличие кнопки подписки через Facebook
    viber = models.NullBooleanField(verbose_name='Viber')  # наличие кнопки подписки через Viber
    subs_list = models.ForeignKey(SubsList, verbose_name='SubsList', on_delete=models.CASCADE)  # идентификатор подписного листа
    image = models.ForeignKey(Images, verbose_name='Images', null=True, blank=True)  # изображениe
    phone = models.NullBooleanField(verbose_name='Phone')  # наличие поля для телефона
    timer_date = models.DateTimeField(verbose_name='TimerDate', null=True, blank=True)  # таймер обратного отсчета до определенной даты
    local_time = models.NullBooleanField(verbose_name='LocalTime')  # True-дата определяется по локальному времени пользователя
    timer_interval = models.TimeField(verbose_name='TimerInterval', null=True, blank=True)  # таймер обратного отсчета на промежуток времени
    right_now = models.NullBooleanField(verbose_name='RightNow')  # True-начало отсчета прямо сейчас, False-с первого посещения сайта
    utp = models.CharField(verbose_name='Utp', max_length=45, null=True, blank=True)  # уникальное торговое предложение по окончании таймера
    cta = models.CharField(verbose_name='Cta', max_length=35, null=True, blank=True)  # призыв к действию по окончании таймера
    confidentiality = models.TextField(verbose_name='Confidentiality', max_length=300)  # ссылка на страницу политики конфиденциальности
    user = models.ForeignKey(User, verbose_name='Client', on_delete=models.CASCADE)  # клиент, создавший форму подписки
    created_date = models.DateTimeField(verbose_name='CreatedDate', auto_now=True)  # дата создания формы подписки
    deleted = models.NullBooleanField(verbose_name='Deleted')  # True-удален, т.е. перенесен в архив, False/null - действующий

    class Meta:
        verbose_name = 'Subscription blank'
        verbose_name_plural = 'Subscription blanks'

    def __str__(self):
        return self.title
