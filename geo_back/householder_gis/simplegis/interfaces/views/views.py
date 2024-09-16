import warnings

from django.db.models import Q
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from householder_gis.simplegis.logic import calculate_geometry
from householder_gis.simplegis.models import BusStop, House, Metro, Shop
from householder_gis.simplegis.serrializers import (
    AddDistanceSerializer,
    RegisterUserSerializer,
    ShowZoneSerializer,
    MetroStationSerializer,
    BusStopSerializer,
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

warnings.filterwarnings("ignore")


class ShowZone(APIView):
    serializer_class = ShowZoneSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    @extend_schema(
        parameters=[ShowZoneSerializer],
        responses={200: None},
    )
    def get(self, request: Request, *args, **kwargs) -> JsonResponse:
        serializer = ShowZoneSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        type_iso = serializer.validated_data.get("type_iso")
        time_iso = serializer.validated_data.get("time_iso")
        longitude = serializer.validated_data.get("lon")
        latitude = serializer.validated_data.get("lat")

        speed = 25
        if type_iso == "walk":
            speed = 4.5

        distance = speed * time_iso / 60

        quarters_count = House.objects.get_quaters_in_R(longitude, latitude, distance)[
            "quarters_count"
        ]
        shops = Shop.objects.get_shops_in_R(longitude, latitude, distance)
        our_shops_for_render = shops.filter(name="Электротовары")
        opponents_for_render = shops.filter(~Q(name="Электротовары"))
        bus_station, bus_stop_count, routes_count = BusStop.objects.get_stops_in_R(
            longitude, latitude, dist=0.3
        )
        # metro_count = Metro.objects.get_stations_in_R(longitude, latitude, distance)
        metro_stations_service = MetroStations(
            longitude=longitude, latitude=latitude, distance=distance
        )
        metro_count = metro_stations_service.get_stations_inside_circle_zone(
            longitude, latitude, distance
        )

        iso_poly = calculate_geometry.get_R((latitude, longitude), distance)

        geojson = {
            "type": "FeatureCollection",
            "features": {
                "type": "Feature",
                "properties": {
                    "type_iso": (
                        "автомобиль" if type_iso == "drive_service" else "пешком"
                    ),
                    "time_iso": time_iso,
                    "quarters_count": quarters_count,
                    "bus_station": BusStopSerializer(bus_station, many=True).data,
                    "bus_stop_count": bus_stop_count,
                    "metro_count": MetroStationSerializer(metro_count, many=True).data,
                    "routes_count": routes_count,
                    "opponents_for_render": AddDistanceSerializer(
                        opponents_for_render, many=True
                    ).data,
                    "our_shops_for_render": AddDistanceSerializer(
                        our_shops_for_render, many=True
                    ).data,
                    "pin_coords": [longitude, latitude],
                },
                "geometry": iso_poly,
            },
        }

        return JsonResponse(geojson, status=200)


class RegistrationAPIView(APIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        refresh.payload.update({"user_id": user.id, "username": user.username})

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )
