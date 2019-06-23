import pandas
from flask import g
from app.models.geo import GeoPoint

def get_db():
    if 'db' not in g:
        g.db = TrailDatabase()

    return g.db

class Trail:
   def __init__(self, name, cluster, latitude, longitude, themes = []):
      self.name = name
      self.cluster = int(cluster)
      self.themes = themes
      self.coordinates = GeoPoint(latitude, longitude)

class TrailDatabase:

   def __init__(self):
       self.trails_db = pandas.read_csv( './app/static/data/trail_geotags_clusters1.csv')


   def find_by_name(self, name_query):
       trails_data = self.trails_db[self.trails_db['trail']== name_query]

       if(len(trails_data)==0):
            return False
       trails_data = trails_data.to_dict('records')
       trail_data = trails_data[0]
       themes = create_tags_list(trail_data);
       trail = Trail(name = trail_data['trail'], cluster = trail_data['cluster'], latitude = trail_data['latitude'], longitude = trail_data['longitude'], themes = themes)
       return trail

   def get_all_by_cluster(self, cluster_query):
       trail_data = self.trails_db[self.trails_db['cluster']== cluster_query]
       result = []
       for row in trail_data.to_dict('records'):
           themes = create_tags_list(row);
           result.append(Trail(name = row['trail'], cluster = row['cluster'], latitude = row['latitude'], longitude = row['longitude'], themes = themes))
       return result


def create_tags_list(attributes):
        exclude = ['trail', 'cluster','length', 'elevation', 'latitude', 'longitude'];
        theme_values = {}
        for key in attributes:
            if(key not in exclude and attributes[key] > 0):
                theme_values[key] = attributes[key]
        sorted_names = sorted(theme_values, key=lambda x: theme_values[x], reverse=True)
        
        return sorted_names[0:5]
