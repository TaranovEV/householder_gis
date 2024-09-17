from dataclasses import dataclass
from functools import partial
from typing import List

import geopandas as gpd
import pyproj
from shapely.geometry import Point, Polygon
from shapely.ops import transform

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)


@dataclass(slots=True, kw_only=True)
class Isochron:
    longitude: Longitude
    latitude: Latitude
    radius: float

    def get_pyproj_transform_settings(self):
        proj_wgs84 = pyproj.Proj("+proj=longlat +datum=WGS84")
        aeqd_proj = "+proj=aeqd +lat_0={lat} +lon_0={lon} +x_0=0 +y_0=0"
        projection = partial(
            pyproj.transform,
            pyproj.Proj(aeqd_proj.format(lat=self.latitude, lon=self.longitude)),
            proj_wgs84,
        )
        print(type(projection))
        return projection

    def get_buffer(self):
        print(type(Point(0, 0).buffer(self.radius * 1000)))
        return Point(0, 0).buffer(self.radius * 1000)

    def get_point_list(self, projection, buffer):
        transformed_points = transform(projection, buffer).exterior.coords[:]
        point_list = [Point(x) for x in transformed_points]
        print(type(point_list))
        return point_list

    def transform_point_list_to_geodataframe(
        self, point_list: List
    ) -> gpd.GeoDataFrame:
        circle_in_geo_df = gpd.GeoDataFrame()
        circle_in_geo_df["geometry"] = None
        circle_in_geo_df.loc[0, "geometry"] = Polygon([(p.x, p.y) for p in point_list])
        circle_in_geo_df.set_crs(epsg=4326, inplace=True)
        return circle_in_geo_df

    def get_list_coordinates_cirlce(self, circle_in_geo_df: gpd.GeoDataFrame) -> List:
        print(type(circle_in_geo_df["geometry"][0].exterior.coords[0]))
        return list(circle_in_geo_df["geometry"][0].exterior.coords)

    def get_circle(self) -> List:
        projection = self.get_pyproj_transform_settings()
        buffer = self.get_buffer()
        point_list = self.get_point_list(projection=projection, buffer=buffer)
        circle_in_geo_df = self.transform_point_list_to_geodataframe(
            point_list=point_list
        )
        return self.get_list_coordinates_cirlce(circle_in_geo_df=circle_in_geo_df)
