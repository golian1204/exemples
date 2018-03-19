from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from mess.models.dialogs import YesNoAnswer
from mess.serializers.dialogs import YesNoAnswerSerializer


class YesNoAnswerList(LoggingMixin, generics.GenericAPIView):
    queryset = YesNoAnswer.objects.all()
    serializer_class = YesNoAnswerSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = YesNoAnswer.objects.all()
        mess_id = self.request.query_params.get('mess_id', None)
        if mess_id is not None:
            queryset = queryset.filter(mess_id=mess_id)
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


class YesNoAnswerDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = YesNoAnswerSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, pk, format=None):
        try:
            yes_no_answer = YesNoAnswer.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(yes_no_answer)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        yes_no_answer = YesNoAnswer.objects.get(pk=pk)
        serializer = self.get_serializer(yes_no_answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        yes_no_answer = YesNoAnswer.objects.get(pk=pk)
        yes_no_answer.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_200_OK)
