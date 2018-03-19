from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from subscriptions.models.subscribers import Subscribers, Subscriptions
from subscriptions.serializers.subscribers import SubscribersSerializer, SubscriptionsSerializer


class SubscribersList(LoggingMixin, generics.GenericAPIView):
    queryset = Subscribers.objects.all()
    serializer_class = SubscribersSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = Subscribers.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        bot_id = self.request.query_params.get('bot_id', None)
        chat_bot = self.request.query_params.get('chat_bot', None)
        if bot_id is not None and chat_bot is not None:
            queryset = queryset.filter(bot_id=bot_id, chat_bot=chat_bot)
        elif user_id is not None:
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


class SubscribersDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = SubscribersSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, pk, format=None):
        try:
            subscriber = Subscribers.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(subscriber)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        subscriber = Subscribers.objects.get(pk=pk)
        serializer = self.get_serializer(subscriber, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subscriber = Subscribers.objects.get(pk=pk)
        subscriber.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_200_OK)


class SubscriptionsList(LoggingMixin, generics.GenericAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = Subscriptions.objects.all()
        subs_list_id = self.request.query_params.get('subs_list', None)
        subscriber_id = self.request.query_params.get('subscriber', None)
        if subs_list_id is not None and subscriber_id is None:
            queryset = queryset.filter(subs_list_id=subs_list_id)
        elif subs_list_id is None and subscriber_id is not None:
            queryset = queryset.filter(subscriber_id=subscriber_id)
        elif subs_list_id is not None and subscriber_id is not None:
            queryset = queryset.filter(subs_list_id=subs_list_id, subscriber_id=subscriber_id)
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


class SubscriptionsDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = SubscriptionsSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, pk, format=None):
        try:
            subscription = Subscriptions.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(subscription)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        subscription = Subscriptions.objects.get(pk=pk)
        serializer = self.get_serializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subscription = Subscriptions.objects.get(pk=pk)
        subscription.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_200_OK)
