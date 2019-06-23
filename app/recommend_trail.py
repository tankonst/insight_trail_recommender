import pandas as pd
import folium
from app.models.Trail import get_db
from app.models.geo import GeoArea, GeoPoint, radius

def load_data(csv_file):
    trails_db = pd.read_csv(csv_file)
    return trails_db


def similar_trails(trail, area: GeoArea):
    trails_in_cluster = get_db().get_all_by_same_cluster(trail)
    trails_in_cluster_by_radius = []
    for similar_trail in trails_in_cluster:
        distance = radius(area.point, trail.coordinates)
        if(distance < area.radius):
            trails_in_cluster_by_radius.append(similar_trail)
    return trails_in_cluster_by_radius


def mapping_trails(trail_group, center_point: GeoPoint):
    # create the map
    m = folium.Map(location=[center_point.latitude, center_point.longitude], zoom_start=7)
    for trail in trail_group:
        # put markers on the map
        folium.Marker([trail.coordinates.latitude, trail.coordinates.longitude], popup=trail.name).add_to(m)
    map_name = './app/static/map_cluster.html'
    m.save(map_name)
    print('map is saved')
