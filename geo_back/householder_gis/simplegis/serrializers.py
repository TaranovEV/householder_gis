from django.contrib.auth.models import User
from householder_gis.simplegis.models import Shop, Metro, BusStop
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class ShowZoneSerializer(serializers.Serializer):
    lat = serializers.FloatField(required=True)
    lon = serializers.FloatField(required=True)
    type_iso = serializers.CharField(required=True)
    time_iso = serializers.IntegerField(required=True)


class AddDistanceSerializer(GeoFeatureModelSerializer):
    distance = serializers.SerializerMethodField()

    def get_distance(self, obj):
        try:
            return obj.distance.m
        except:
            return None

    class Meta:
        model = Shop
        geo_field = "geometry"
        fields = "__all__"


class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User(email=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class MetroStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metro
        geo_field = "geometry"
        fields = "__all__"


class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        geo_field = "geometry"
        fields = "__all__"
