from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from mess.models.statistics import YesNoStatistic
from mess.serializers.statistics import YesNoStatisticSerializer
from mess.models.dialogs import YesNoAnswer
from subscriptions.models.subscribers import Subscribers
from mess.models.mess import MessStatus
from datetime import datetime


class YesNoStatisticList(LoggingMixin, generics.GenericAPIView):
    queryset = YesNoStatistic.objects.all()
    serializer_class = YesNoStatisticSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = YesNoStatistic.objects.all()
        mess_id = self.request.query_params.get('mess_id', None)
        subscriber_id = self.request.query_params.get('subscriber_id', None)
        if mess_id is not None and subscriber_id is not None:
            queryset = queryset.filter(mess_id=mess_id, subscriber_id=subscriber_id)
        elif mess_id is not None:
            queryset = queryset.filter(mess_id=mess_id)
        elif subscriber_id is not None:
            queryset = queryset.filter(subscriber_id=subscriber_id)
        return queryset

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    @staticmethod
    def yes_no_answer(statistics_data):
        """Подбор следующего месса для отправки подписчику, взависимости от его ответа Да/Нет"""

        yes = statistics_data.get('yes')
        if yes is not None:  # если подписчика кликнул Да или Нет
            mess = statistics_data.get('mess')
            # Получаем для мессы для кнопок Да-Нет
            try:
                yes_no_answer = YesNoAnswer.objects.get(mess_id=mess)
            except ObjectDoesNotExist:
                yes_no_answer = None
            if yes_no_answer:
                # Определяем следующий месс в зависимости от выбора подписчика Да или Нет
                next_mess = yes_no_answer.yes if yes else yes_no_answer.no
                if next_mess:
                    subscriber = statistics_data.get('subscriber')
                    subscriber_data = Subscribers.objects.get(pk=subscriber)
                    return next_mess, subscriber_data
        return None, None

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            next_mess, subscriber = self.yes_no_answer(request.data)
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


class YesNoStatisticDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = YesNoStatisticSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, pk, format=None):
        try:
            yes_no_statistic = YesNoStatistic.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(yes_no_statistic)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        yes_no_statistic = YesNoStatistic.objects.get(pk=pk)
        serializer = self.get_serializer(yes_no_statistic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        yes_no_statistic = YesNoStatistic.objects.get(pk=pk)
        yes_no_statistic.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_200_OK)
