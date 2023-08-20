from rest_framework import serializers

from api.models import Ad, MarkaModel, MarkaVehicle


class AdSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    marka = serializers.CharField(source='marka.name')

    class Meta:
        model = Ad
        fields = ('id', 'user', 'marka', 'type_rudder', 'type_vehicle', 'type_transmission', 'type_drive', 'type_body',
                  'type_engine', 'date', 'type_ad')


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkaVehicle
        fields = ('name', 'marka')
