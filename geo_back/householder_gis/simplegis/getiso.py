import math
import numpy as np
import networkx as nx
import osmnx as ox
from shapely.geometry import Point, MultiPolygon, MultiLineString
from shapely.ops import unary_union, polygonize
from scipy.spatial import Delaunay


def alpha_shape(points, alpha):
    """
    @param alpha alpha value to influence the gooeyness of the border.
    When Biggest then lose points
    """

    if len(points) < 4:
        return MultiPolygon((list(points))).convex_hull

    def add_edge(edges, edge_points, coords, i, j):
        if (i, j) in edges or (j, i) in edges:
            return
        edges.add((i, j))
        edge_points.append(coords[[i, j]])

    coords = np.array([point.coords[0] for point in points])

    tri = Delaunay(coords)
    edges = set()
    edge_points = []

    for ia, ib, ic in tri.vertices:
        pa = coords[ia]
        pb = coords[ib]
        pc = coords[ic]

        a = math.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
        b = math.sqrt((pb[0] - pc[0]) ** 2 + (pb[1] - pc[1]) ** 2)
        c = math.sqrt((pc[0] - pa[0]) ** 2 + (pc[1] - pa[1]) ** 2)

        s = (a + b + c) / 2.0

        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        circum_r = a * b * c / (4.0 * area)

        if circum_r < 1.0 / alpha:
            add_edge(edges, edge_points, coords, ia, ib)
            add_edge(edges, edge_points, coords, ia, ib)
            add_edge(edges, edge_points, coords, ia, ib)

    m = MultiLineString(edge_points)
    triangles = list(polygonize(m))

    return unary_union(triangles)

def create_graph(network_type, coord, time_traveling):
    speed = 4.5
    if network_type == 'drive_service':
        speed = 50

    G = ox.graph_from_point(coord,
                            dist_type='network',
                            network_type=network_type,
                            dist=speed*float(time_traveling)/60*1000)

    point_of_interest = ox.distance.nearest_nodes(G, coord[1], coord[0])
    G = ox.project_graph(G)

    if network_type == 'drive_service':
        G = ox.speed.add_edge_speeds(G, fallback=25)

        for _, _, _, data in G.edges(data=True, keys=True):
            data['speed_kph'] = data['speed_kph'] / 1.8
        G = ox.speed.add_edge_travel_times(G)

    elif network_type == 'walk':
        meters_per_minute = 75
        for _, _, _, data in G.edges(data=True, keys=True):
            data['travel_time'] = data['length'] / meters_per_minute

    subgraph = nx.ego_graph(G,
                            point_of_interest,
                            radius=float(time_traveling) * speed,
                            distance='travel_time')
    node_points = [
        Point((data["x"], data["y"])) for node, data in
        ox.project_graph(subgraph, to_crs='epsg:4326').nodes(data=True)
    ]

    return node_points
