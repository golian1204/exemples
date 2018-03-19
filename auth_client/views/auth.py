from django.contrib.auth.models import User

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from users.serializers.users import UserSerializer


class AuthTokenList(LoggingMixin, ObtainAuthToken, generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super(AuthTokenList, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])

        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user)
        return Response({'status': 'success', 'message': None, 'data': {'user': serializer.data, 'token': token.key}}, status=status.HTTP_201_CREATED)


class AuthTokenDetail(LoggingMixin, generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def delete(self, request, pk, format=None):
        token = Token.objects.get(user_id=pk)
        token.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_200_OK)
