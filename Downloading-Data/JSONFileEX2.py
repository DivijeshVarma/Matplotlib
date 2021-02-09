# 16-8. Recent Earthquakes: You can find data files containing information about the most recent earthquakes
# over 1-hour, 1-day, 7-day, and 30-day periods online.
# Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php and you’ll see a list of links to data sets
# for various time periods, focusing on earthquakes of different magnitudes. Download one of these data sets,
# and create a visualization of the most recent earthquake activity.

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Let’s start by loading the data and displaying it in a format that’s easier to read.
# This is a long data file, so instead of printing it, we’ll rewrite the data to a new file.
# Then we can open that file and scroll back and forth eas- ily through the data:

file = 'Data/significant_month_data.json'
with open(file) as f:
    all_eq_data = json.load(f)

# Making a List of All Earthquakes
# readable_file = 'Data/readablesignificant_month_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

# Extracting Magnitudes
# Extracting Location Data
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# print(mags[:10])
# print(lons[:10])
# print(lats[:10])

# # Map the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
title = all_eq_data['metadata']['title']
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')