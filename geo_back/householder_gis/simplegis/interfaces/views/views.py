import warnings

from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from householder_gis.simplegis.serrializers import (
    RegisterUserSerializer,
    ShowZoneSerializer,
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Longitude,
    Latitude,
)
from geo_back.householder_gis.simplegis.services.geodata_layer import (
    GeoDataLayerService,
)
from geo_back.householder_gis.simplegis.services.isochrone import IsochroneService

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
        longitude = Longitude(value=serializer.validated_data.get("lon"))
        latitude = Latitude(value=serializer.validated_data.get("lat"))

        isochrone_service = IsochroneService(
            longitude=longitude, latitude=latitude, type_iso=type_iso, time_iso=time_iso
        )
        isochrone = isochrone_service.isochrone

        geo_data_service = GeoDataLayerService(isochrone=isochrone)
        geo_data_layer = geo_data_service.build_layers()

        return JsonResponse(geo_data_layer.to_json(), status=200)


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
