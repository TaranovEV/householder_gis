import geopandas as gpd
import pyproj

from functools import partial
from shapely.ops import transform
from shapely.geometry import Point, Polygon


def load_geodataframe(path:str):
    gdf = gpd.read_file(path,GEOM_POSSIBLE_NAMES='geometry',
                       KEEP_GEOM_COLUMNS='NO',encoding='utf-8')
    gdf = gpd.GeoDataFrame(gdf, geometry=gdf.geometry)
    gdf.set_crs(epsg=4326, inplace=True)
    return gdf


def get_R(coord:tuple, R:float)->object:
    proj_wgs84 = pyproj.Proj('+proj=longlat +datum=WGS84')
    lat = coord[0]
    lon = coord[1]
    aeqd_proj = '+proj=aeqd +lat_0={lat} +lon_0={lon} +x_0=0 +y_0=0'
    project = partial(
        pyproj.transform,
        pyproj.Proj(aeqd_proj.format(lat=lat, lon=lon)),
        proj_wgs84
    )

    buf = Point(0, 0).buffer(R * 1000)
    pointList = transform(project, buf).exterior.coords[:]
    pointList = [Point(x) for x in pointList]
    CIRCLE = gpd.GeoDataFrame()

    CIRCLE['geometry'] = None
    CIRCLE.loc[0, 'geometry'] = Polygon([(p.x, p.y) for p in pointList])
    CIRCLE.set_crs(epsg=4326, inplace=True)
    return CIRCLE['geometry']
