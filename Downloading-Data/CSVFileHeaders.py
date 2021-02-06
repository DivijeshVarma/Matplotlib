import csv

file = 'Data/sitka_weather_07-2018_simple.csv'
with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
