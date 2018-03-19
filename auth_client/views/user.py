from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from users.models.profiles import Profiles
from users.serializers.users import UserSerializer


class UserDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, hash, format=None):
        try:
            profile = Profiles.objects.get(hash=hash)
            user = User.objects.get(id=profile.user.id)
        except ObjectDoesNotExist:
            return Response({'status': 'error', 'message': None, 'data': None}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(user)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
