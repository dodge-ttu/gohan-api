from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Devicetag

from devices import serializers


class DevicetagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage devicetags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Devicetag.objects.all()
    serializer_class = serializers.DevicetagSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
