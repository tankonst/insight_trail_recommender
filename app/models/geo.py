import math
import pandas as pd

# def get_db():
#     if 'db' not in g:
#         g.db = ZipcodeDatabase()
#     return g.db

class ZipcodeDatabase:

    def __init__(self):
        self.zip_db = pd.read_csv( './app/static/data/us-zip-code-latitude-and-longitude.csv', converters={'Zip': lambda x: str(x)})
        

    def zip_to_point(self, zipcode):
        zip_data = self.zip_db[self.zip_db['Zip'] == zipcode]

        if(len(zip_data)==0):
             return False
        zip_data = zip_data.to_dict('records')
        zip_data = zip_data[0]
        longitude = zip_data['Longitude']
        latitude = zip_data['Latitude']
        return( GeoPoint(latitude, longitude))


class GeoPoint:
    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

class GeoArea:
    def __init__(self, point : GeoPoint, radius):
        self.point = point
        self.radius = float(radius)

def spherical_distance(point1: GeoPoint, point2: GeoPoint):

    angle = math.acos(math.sin(to_radians(point1.latitude))*math.sin(to_radians(point2.latitude))+math.cos(to_radians(point1.latitude))*math.cos(to_radians(point2.latitude))*math.cos(to_radians(point1.longitude-point2.longitude)))
    r_0 = 3958.8 # Earth's radius in miles
    r = r_0*angle
    return r

def to_radians(angle):
    return angle/360*2*math.pi
