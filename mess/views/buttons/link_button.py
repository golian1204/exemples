from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from mess.models.buttons import LinkButton
from mess.serializers.buttons import LinkButtonSerializer


class LinkButtonsList(LoggingMixin, generics.GenericAPIView):
    queryset = LinkButton.objects.all()
    serializer_class = LinkButtonSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

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


class LinkButtonDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = LinkButtonSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, pk, format=None):
        try:
            link_button = LinkButton.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(link_button)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            link_button = LinkButton.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(link_button, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        try:
            link_button = LinkButton.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        link_button.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_200_OK)
