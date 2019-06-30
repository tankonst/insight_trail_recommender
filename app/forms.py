from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import DecimalField
from wtforms.validators import DataRequired
from app.models.geo import GeoArea, GeoPoint, ZipcodeDatabase



class TrailRecommendForm(FlaskForm):
    query = StringField('query', validators=[DataRequired()])
    # latitude = DecimalField('latitude', validators=[DataRequired()])
    # longitude = DecimalField('longitude', validators=[DataRequired()])
    radius = DecimalField('radius', validators=[DataRequired()])
    zipcode = StringField('zipcode', validators=[DataRequired()])

    def getArea(self):
        # point = GeoPoint(latitude=self.latitude.data, longitude=self.longitude.data)
        point = ZipcodeDatabase().zip_to_point(self.zipcode.data)
        print(point.latitude)
        return GeoArea(point=point, radius=self.radius.data)
