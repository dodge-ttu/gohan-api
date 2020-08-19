from rest_framework import serializers
from core.models import Devicetag


class DevicetagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Devicetag
        fields = ('id', 'name')
        read_only_fields = ('id',)
