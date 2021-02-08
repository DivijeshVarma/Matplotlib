import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Let’s start by loading the data and displaying it in a format that’s easier to read.
# This is a long data file, so instead of printing it, we’ll rewrite the data to a new file.
# Then we can open that file and scroll back and forth eas- ily through the data:

file = 'Data/eq_data_1_day_m1.json'
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
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(lons[:10])
# print(lats[:10])

# # Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
