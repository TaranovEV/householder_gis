from rest_framework import serializers

class ShowZoneSerrializer(serializers.Serializer):
    lat = serializers.FloatField(required=True)
    lon = serializers.FloatField(required=True)
    type_iso = serializers.CharField(required=True)
    time_iso = serializers.IntegerField(required=True)
