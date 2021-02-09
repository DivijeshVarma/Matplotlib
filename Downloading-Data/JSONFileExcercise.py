# 16-6. Refactoring: The loop that pulls data from all_eq_dicts uses variables for the magnitude,
# longitude, latitude, and title of each earthquake before appending these values to their appropriate lists.
# This approach was chosen for clarity in how to pull data from a JSON file, but it’s not necessary in your code.
# Instead of using these temporary variables, pull each value from eq_dict and
# append it to the appropriate list in one line. Doing so should shorten the body of this loop to just four lines.

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Let’s start by loading the data and displaying it in a format that’s easier to read.
# This is a long data file, so instead of printing it, we’ll rewrite the data to a new file.
# Then we can open that file and scroll back and forth eas- ily through the data:

# file = 'Data/eq_data_30_day_m1.json'
# with open(file) as f:
#     all_eq_data = json.load(f)
#
# # Making a List of All Earthquakes
# # readable_file = 'Data/readable_eq_data.json'
# # with open(readable_file, 'w') as f:
# #     json.dump(all_eq_data, f, indent=4)
#
# all_eq_dicts = all_eq_data['features']
# # print(len(all_eq_dicts))
#
# # Extracting Magnitudes
# # Extracting Location Data
# mags, lons, lats, hover_texts = [], [], [], []
# for eq_dict in all_eq_dicts:
#     mags.append(eq_dict['properties']['mag'])
#     lons.append(eq_dict['geometry']['coordinates'][0])
#     lats.append(eq_dict['geometry']['coordinates'][1])
#     hover_texts.append(eq_dict['properties']['title'])
#
# # print(mags[:10])
# # print(lons[:10])
# # print(lats[:10])
#
# # # Map the earthquakes.
# # data = [Scattergeo(lon=lons, lat=lats)]
# data = [{
#     'type': 'scattergeo',
#     'lon': lons,
#     'lat': lats,
#     'text': hover_texts,
#     'marker': {
#         'size': [5*mag for mag in mags],
#         'color': mags,
#         'colorscale': 'Viridis',
#         'reversescale': True,
#         'colorbar': {'title': 'Magnitude'},
#     }
# }]
# my_layout = Layout(title='Global Earthquakes')
#
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='global_earthquakes.html')

# 16-7. Automated Title: In this section, we specified the title manually when defining my_layout,
# which means we have to remember to update the title every time the source file changes.
# Instead, you can use the title for the data set in the metadata part of the JSON file. Pull this value,
# assign it to a variable, and use this for the title of the map when you’re defining my_layout.

file = 'Data/eq_data_30_day_m1.json'
with open(file) as f:
    all_eq_data = json.load(f)

# Making a List of All Earthquakes
# readable_file = 'Data/readable_eq_data.json'
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
layout_title = all_eq_data['metadata']['title']
my_layout = Layout(title=layout_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')