from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Devicetype, Device, Location, Wxstatreading

from devices import serializers


class BaseSensorAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base view set for user owned sensor attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Create a new item"""
        serializer.save(user=self.request.user)


class DeviceViewSet(BaseSensorAttrViewSet):
    """Manage specific device in the database"""
    queryset = Device.objects.all()
    serializer_class = serializers.DeviceSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-device_id')


class DevicetypeViewSet(BaseSensorAttrViewSet):
    """Manage devices in the database"""
    queryset = Devicetype.objects.all()
    serializer_class = serializers.DevicetypeSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user"""
        return self.queryset.order_by('-device_type')

    def perform_create(self, serializer):
        """Create a new item"""
        return serializer.save()


class LocationViewSet(BaseSensorAttrViewSet):
    """Manage locations in the database"""
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('loc_id')


class WxstatreadingViewSet(BaseSensorAttrViewSet):
    """Manage weather statio readings in the database"""
    queryset = Wxstatreading.objects.all()
    serializer_class = serializers.WxstatreadingSerializer

    def get_queryset(self):
        """Get objects for current authenticated user and location"""
        loc = self.request.query_params.get('loc', None)
        if loc is not None:
            return self.queryset.filter(
                user=self.request.user,
                loc=loc
            )
        else:
            return self.queryset.filter(
                user=self.request.user
            )
