from django.db import models
from mess.models.mess import Mess
from django.contrib.auth.models import User
from subscriptions.models.subscribers import Subscribers


class Dialogs(models.Model):
    """Диалог бота с подписчиком"""

    user = models.ForeignKey(User, verbose_name='Client', on_delete=models.CASCADE)  # Идентификатор клиента
    subscriber = models.ForeignKey(Subscribers, verbose_name='Subscriber', on_delete=models.CASCADE)  # Идентификатор подписичика

    class Meta:
        verbose_name = 'Dialog'
        verbose_name_plural = 'Dialogues'
        unique_together = ('user', 'subscriber')

    def __str__(self):
        return str(self.pk)


class Messages(models.Model):
    """Сообщения в диалоге"""

    dialog = models.ForeignKey(Dialogs, verbose_name='Dialog', on_delete=models.CASCADE)  # Идентификатор диалога
    user_sender = models.BooleanField(verbose_name='UserSender', default=False)  # True-отправтель Бот клиента, False-отправитель подписчик
    text = models.TextField(verbose_name='Text', null=True, blank=True)  # Текст сообщения, не заполняется, если отправлен Mess
    mess = models.ForeignKey(Mess, verbose_name='Mess', null=True, blank=True, on_delete=models.SET_NULL)  # Идентификатор Mess, если был отправлен Mess
    send_date = models.DateTimeField(verbose_name='SendDate', auto_now_add=True)  # Дата отправки (пригодится для сортировке по дате)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return str(self.pk)


class AutoAnswer(models.Model):
    """Автоматический ответ подписчику на основе ключевых и минус слов"""

    user = models.ForeignKey(User, verbose_name='Client', on_delete=models.CASCADE, related_name='auto_answers')  # Идентификатор клиента
    key_word = models.TextField(verbose_name='KeyWord')  # Ключевые слова (вызывающие автоответ)
    anti_word = models.TextField(verbose_name='AntiWord', null=True, blank=True)  # Минус слова (отменяющие автоответ)
    mess = models.ForeignKey(Mess, verbose_name='Mess', null=True, blank=True, on_delete=models.CASCADE)  # Идентификатор Mess
    create_date = models.DateTimeField(verbose_name='CreateDate', auto_now=True)  # Дата создания автоотета

    class Meta:
        verbose_name = 'AutoAnswer'
        verbose_name_plural = 'AutoAnswers'

    def __str__(self):
        return str(self.pk)


class YesNoAnswer(models.Model):
    """Запрограмированные мессы для кнопок Да-Нет"""

    mess = models.OneToOneField(Mess, verbose_name='Mess', null=True, blank=True, on_delete=models.SET_NULL)  # идентификатор Mess, содержащего кнопки Да/Нет
    yes = models.ForeignKey(Mess, verbose_name='Yes', null=True, blank=True, on_delete=models.SET_NULL, related_name='yes_answer')  # идентификатор Mess, отправляемого при  выборе Да
    no = models.ForeignKey(Mess, verbose_name='No', null=True, blank=True, on_delete=models.SET_NULL, related_name='no_answer')  # идентификатор Messa, отправляемого при выборе Нет

    class Meta:
        verbose_name = 'YesNoAnswer'
        verbose_name_plural = 'YesNoAnswers'

    def __str__(self):
        return str(self.pk)

