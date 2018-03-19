from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from users.models.profiles import Profiles
from users.serializers.profiles import ProfilesSerializer

class ProfileDetail(LoggingMixin, generics.GenericAPIView):
    serializer_class = ProfilesSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser,)

    def get(self, request, user_id, format=None):
        profile = Profiles.objects.get(user_id=user_id)
        serializer = self.serializer_class(profile)
        return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, user_id, format=None):
        profile = Profiles.objects.get(user_id=user_id)
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': serializer.error_messages, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        profile = Profiles.objects.get(user_id=user_id)
        profile.delete()
        return Response({'status': 'success', 'message': None, 'data': None}, status=status.HTTP_204_NO_CONTENT)
