import csv

file = 'Data/sitka_weather_07-2018_simple.csv'
with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

# The enumerate() function returns both the index of each item and the value of each item as you loop through a list.
for index, column_header in enumerate(header_row):
    print(index, column_header)
