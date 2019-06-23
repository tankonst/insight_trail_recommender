import pandas as pd
import re


def autocomplete_trail(query):
    trails = ''
    dbname = './app/static/data/trail_clusters_new.csv'
    trails_db = pd.read_csv(dbname)

    trails = {trail for trail in trails_db['trail']}
    result = [];
    regexp  = re.compile('.*'+query+'.*', re.I)
    for trail in trails:
        if  re.match(regexp, trail) and len(result) < 15:
             result.append(trail);

    return result
