from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from mess.models.dialogs import Messages, Dialogs
from mess.models.mess import MessStatus
from mess.serializers.dialogs import MessagesSerializer
from datetime import datetime
import re
from pprint import pprint


class MessagesList(LoggingMixin, generics.GenericAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = Messages.objects.all()
        dialog_id = self.request.query_params.get('dialog_id', None)
        if dialog_id is not None:
            queryset = queryset.filter(dialog_id=dialog_id)
        return queryset

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    @staticmethod
    def auto_answer(message_data):
        """Подбор автоответа для сообщения подписчика"""

        message_text = message_data.get('text')
        if message_text:  # если от подписчика получено сообщение с текстом
            dialog = message_data.get('dialog')  # получаем id диалога
            # По id диалога получаем id клиента
            try:
                dialog_data = Dialogs.objects.get(pk=dialog)
            except ObjectDoesNotExist:
                dialog_data = None
            if dialog_data:
                # Форматируем текст сообщения
                message_text = ' {} '.format(' '.join(re.findall('(\w+?)\W', message_text + ' '))).lower()
                # По id клиента получаем список автоответов
                user = dialog_data.user
                auto_answers = user.auto_answers.all() or []

                def _handling_words(words):
                    """Обработка строки с ключевыми или минус словами"""
                    words = [word.strip() for word in words.split(',')]
                    words = [' {} '.format(word.replace('\"', '')).lower() for word in words]
                    return words

                for auto_answer in auto_answers:
                    # Получаем для автоответа 'ключевые слова', вызывающие автоответ
                    key_words = _handling_words(auto_answer.key_word)
                    send = [word for word in key_words if word in message_text]
                    if send:  # если ключевые слова входят в текст сообщения
                        # Получаем для автоответа 'минус слова', отменяющие автоответ
                        anti_words = _handling_words(auto_answer.anti_word)
                        stop = [word for word in anti_words if word in message_text]
                        if not stop:  # если минус слова отсутствуют в тексте сообщения
                            return auto_answer.mess, dialog_data.subscriber
        return None, None

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            next_mess, subscriber = self.auto_answer(request.data)
            if next_mess is not None and subscriber is not None:
                # Создаем месс_статус
                # mess.tasks извлекает из таблицы MessStatus все статусы с process_status=create и отправляет их
                mess_status = MessStatus(mess=next_mess,
                                         subscriber=subscriber,
                                         plan_send_date=datetime.now(),
                                         process_status=MessStatus.CREATE)
                mess_status.save()

            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MessageDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = MessagesSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, pk, format=None):

        try:
            dialog = Messages.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(dialog)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            dialog = Messages.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(dialog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        try:
            dialog = Messages.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        dialog.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_200_OK)
