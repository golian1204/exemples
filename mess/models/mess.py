from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from subscriptions.models.subscribers import Subscribers
from mess.models.attachments import Audios, Videos, Files, Images
from mess.models.buttons import LinkButton, Payment
from mess.models.feedback import Valuation
from mess.models.polls import Interview


class Mess(models.Model):
    """Модель сообщения Mess"""

    # Todo title сделать уникальным, когда будет проверка на фронте на уникальность
    title = models.CharField(verbose_name='Title', max_length=40)  # Название сообщения
    text = models.TextField(verbose_name='Text', max_length=1000)  # Текст сообщения
    images = models.ForeignKey(Images, verbose_name='Images', null=True, blank=True)  # Изображения
    videos = models.ForeignKey(Videos, verbose_name='Videos', null=True, blank=True)  # Видео
    audios = models.ForeignKey(Audios, verbose_name='Audios', null=True, blank=True)  # Аудио
    files = models.ForeignKey(Files, verbose_name='Files', null=True, blank=True)  # Файлы
    interview = models.ForeignKey(Interview, verbose_name='Interview', null=True, blank=True)  # Опрос
    valuation = models.ForeignKey(Valuation, verbose_name='Valuation', null=True, blank=True)  # Оценка
    yesno = models.NullBooleanField(verbose_name='YesNo')  # Наличие кнопок Да-Нет
    like = models.NullBooleanField(verbose_name='Like')  # Наличие кнопок Лайк-Дизлайк
    invite = models.NullBooleanField(verbose_name='Invite')  # Наличие кнопки Пригласить друга
    telegram = models.NullBooleanField(verbose_name='Telegram')  # Наличие кнопки шаринга в Telegram
    facebook = models.NullBooleanField(verbose_name='Facebook')  # Наличие кнопки шаринга в Facebook
    viber = models.NullBooleanField(verbose_name='Viber')  # Наличие кнопки шаринга в Viber
    link_button = models.ForeignKey(LinkButton, verbose_name='LinkButton', null=True, blank=True)  # Кнопка со ссылкой
    payment = models.ForeignKey(Payment, verbose_name='Payment', null=True, blank=True)  # Кнопка оплаты
    created_date = models.DateTimeField(verbose_name='Created date', auto_now=True)  # Дата создания сообщения
    user = models.ForeignKey(User, verbose_name='Client', on_delete=models.CASCADE)  # Клиент, под которым создан Mess
    draft = models.NullBooleanField(verbose_name='Draft')  # Черновик
    time_before = models.DateTimeField(verbose_name='TimeBefore', null=True, blank=True)  # Таймер обратного отсчета до определенной даты
    time_after = models.DateTimeField(verbose_name='TimeAfter', null=True, blank=True)  # Таймер обратного отсчета c момента прочтения
    subs_online = models.NullBooleanField(verbose_name='SubsOnline')  # Отправлять подписчикам онлайн
    deleted = models.NullBooleanField(verbose_name='Deleted')  # True-удален, т.е. перенесен в архив, False/null - действующий

    class Meta:
        verbose_name = 'Mes'
        verbose_name_plural = 'Mess'

    def __str__(self):
        return self.title


class MessStatus(models.Model):
    """Статус Mess"""

    CREATE = 0
    QUEUE = 1
    SENT_TO_API_MESSAGE = 2
    DELIVERED = 3
    READ = 4
    ACTION = 5

    STATUS_CHOICES = (
        (CREATE, 'Создано'),
        (QUEUE, 'В очередеди'),
        (SENT_TO_API_MESSAGE, 'Отправлено на api_message'),
        (DELIVERED, 'Доставлено'),
        (READ, 'Прочитано'),
        (ACTION, 'Совершено действие'),
    )

    mess = models.ForeignKey(Mess, verbose_name='Mess', on_delete=models.CASCADE)  # Идентификатор Messa
    subscriber = models.ForeignKey(Subscribers, verbose_name='Subscriber', on_delete=models.CASCADE)  # Идентификатор подписчика
    plan_send_date = models.DateTimeField(verbose_name='PlanSendDate', null=True, blank=True)  # Запланированная дата отправки сообщения
    create_date = models.DateTimeField(verbose_name='CreateDate', auto_now_add=True)  # Дата создания статуса (клиент кликнул отправить)
    send_date = models.DateTimeField(verbose_name='SendDate', null=True, blank=True)  # Дата отправки (фактическая дата отправки)
    delivery_date = models.DateTimeField(verbose_name='DeliveryDate', null=True, blank=True)  # Дата доставки
    read_date = models.DateTimeField(verbose_name='ReadDate', null=True, blank=True)  # Дата прочтения
    action_date = models.DateTimeField(verbose_name='ActionDate', null=True, blank=True)  # Дата реакции подписчика (например, кликнул да/нет)
    process_status = models.IntegerField(verbose_name='ProcessStatus', choices=STATUS_CHOICES, default=CREATE)  # Статус процесса

    class Meta:
        verbose_name = 'MessStatus'
        verbose_name_plural = 'MessStatuses'
        unique_together = ('mess', 'subscriber')

    def __str__(self):
        return self.mess.title

