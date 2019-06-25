import pandas
from flask import g
from app.models.geo import GeoPoint
import math

def get_db():
    if 'db' not in g:
        g.db = TrailDatabase()

    return g.db

class Trail:
   def __init__(self, name, cluster, latitude, longitude,  labels,tags = []):
      self.name = name
      self.cluster = int(cluster)
      self.tags = tags
      self.coordinates = GeoPoint(latitude, longitude)
      self.labels = labels

class TrailDatabase:

   def __init__(self):
       self.trails_db = pandas.read_csv( './app/static/data/trail_geotags_clusters1.csv')


   def find_by_name(self, name_query):
       trails_data = self.trails_db[self.trails_db['trail']== name_query]

       if(len(trails_data)==0):
            return False
       trails_data = trails_data.to_dict('records')
       trail_data = trails_data[0]
       tags = create_tags_list(trail_data)
       labels = create_labels_vector(trails_data[0])
       # print(labels)
       trail = Trail(name = trail_data['trail'], cluster = trail_data['cluster'], latitude = trail_data['latitude'], longitude = trail_data['longitude'], tags = tags, labels = labels)
       return trail

   def get_all_by_same_cluster(self, trail: Trail):
       ''' Search for trails within the same cluster as the input trail's '''
       trail_data = self.trails_db[self.trails_db['cluster']== trail.cluster]
       result = []
       for row in trail_data.to_dict('records'):
           tags = create_tags_list(row)
           labels = create_labels_vector(row)
           if( not set(tags).isdisjoint(trail.tags)):
                result.append(Trail(name = row['trail'], cluster = row['cluster'], latitude = row['latitude'], longitude = row['longitude'], tags = tags, labels = labels))
       return result


def create_tags_list(attributes):
        exclude = ['trail', 'cluster','length', 'elevation', 'latitude', 'longitude']
        theme_values = {}
        for key in attributes:
            if(key not in exclude and attributes[key] > 0):
                theme_values[key] = attributes[key]
        sorted_names = sorted(theme_values, key=lambda x: theme_values[x], reverse=True)

        return sorted_names[0:5]

def create_labels_vector(row):
    '''Get all labels of the trail'''
    not_labels = ['trail', 'cluster','latitude', 'longitude']
    return {x: row[x] for x in row if x not in not_labels}



def calculate_similarity(trail1: Trail, trail2: Trail):
    trail1_length_squared = 0
    trail2_length_squared = 0
    multiplication = 0
    for key in trail1.labels:
        trail1_length_squared += trail1.labels[key]**2
        trail2_length_squared += trail2.labels[key]**2
        multiplication += trail1.labels[key]*trail2.labels[key]
    if (trail1_length_squared !=0 and trail2_length_squared !=0):
        cosine_similarity = multiplication/math.sqrt(trail1_length_squared)/math.sqrt(trail2_length_squared)
    else:
        cosine_similarity = 0
    return(cosine_similarity)
