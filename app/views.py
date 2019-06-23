from app import app
from flask import request
import pandas as pd
from flask import render_template
import re
import json
from app import recommend_trail as rt
from app import autocomplete_trail as at
from app.forms import TrailRecommendForm
import datetime

from app.models.Trail import get_db


@app.route('/', methods = ['POST', 'GET'])
def index():
    form = TrailRecommendForm()
    trails = []
    themes = []
    recommended_trails_tags = []
    timestamp = datetime.datetime.now()

    if(form.validate_on_submit()):
        trail = get_db().find_by_name(form.query.data)
        if(trail == False):
            return render_template('/search_empty.html', form=form)

        area = form.getArea()
        # getting the list of trails and the cluster number
        similar_trails = rt.similar_trails(trail = trail, area = area)
        print(similar_trails)

        # positioning all trails from the cluster on the NY map
        rt.mapping_trails(similar_trails, center_point = area.point)

        return render_template('/search_results.html', similar_trails=similar_trails,  form=form, timestamp = timestamp, trail = trail )

    return render_template('/search_default.html', form=form)

@app.route('/autocomplete', methods = ['GET'])
def autocomplete():
    query = request.args.get('term')
    return json.dumps(at.autocomplete_trail(query))
