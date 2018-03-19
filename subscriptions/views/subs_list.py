from django.core.exceptions import ObjectDoesNotExist
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from subscriptions.models.subs_list import SubsList
from subscriptions.serializers.subs_list import SubsListSerializer


class SubsListList(LoggingMixin, generics.GenericAPIView):
    queryset = SubsList.objects.all()
    serializer_class = SubsListSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = SubsList.objects.all()
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


class SubsListDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = SubsListSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, pk, format=None):
        try:
            subs_list = SubsList.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(subs_list)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            subs_list = SubsList.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(subs_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        try:
            subs_list = SubsList.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        subs_list.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_200_OK)


class SubsListUUIDDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = SubsListSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, uuid, format=None):
        try:
            subs_list = SubsList.objects.get(uuid=uuid)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(subs_list)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
