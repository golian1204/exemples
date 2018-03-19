from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from bots.models.bots import Bots
from bots.serializers.bots import BotsSerializer


class BotstList(LoggingMixin, generics.GenericAPIView):
    queryset = Bots.objects.all()
    serializer_class = BotsSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = Bots.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BotDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = BotsSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, pk, format=None):
        try:
            bot = Bots.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(bot)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            bot = Bots.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(bot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        try:
            bot = Bots.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        bot.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_200_OK)
