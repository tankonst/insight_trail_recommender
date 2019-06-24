import math

class GeoPoint:
    def __init__(self, latitude, longitude):
       self.latitude = float(latitude)
       self.longitude = float(longitude)

class GeoArea:
    def __init__(self, point : GeoPoint, radius):
        self.point = point
        self.radius = float(radius)

def spherical_distance(point1: GeoPoint, point2: GeoPoint):
    print(point1.latitude)
    angle = math.acos(math.sin(to_radians(point1.latitude))*math.sin(to_radians(point2.latitude))+math.cos(to_radians(point1.latitude))*math.cos(to_radians(point2.latitude))*math.cos(to_radians(point1.longitude-point2.longitude)))
    r_0 = 3958.8 # Earth's radius in miles
    r = r_0*angle
    return r

def to_radians(angle):
    return angle/360*2*math.pi
