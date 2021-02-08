# # 16-1. Sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair amount of rainfall.
# # In the data file sitka_weather_2018_simple.csv is a header called PRCP, which represents daily rainfall amounts.
# # Make a visualization focusing on the data in this column.
# # You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert.
#
import csv
import matplotlib.pyplot as plt
from datetime import datetime
#
# file = 'Data/sitka_weather_2018_simple.csv'
# with open(file) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     # The enumerate() function returns both the index of each item and the value of each item as you loop through a list
#     # for index, column_header in enumerate(header_row):
#     #     print(index, column_header)
#
#     # getting rainfall from file
#     dates, rains = [], []
#
#     for data in reader:
#         current_date = datetime.strptime(data[2], '%Y-%m-%d')
#         rain = float(data[3])
#         dates.append(current_date)
#         rains.append(rain)
#
# # plot High temp
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, rains, c='blue')
#
# # Format plot
# plt.title("daily rainfall amounts 2018", fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel('Rainfall (inch)', fontsize=16)
# fig.autofmt_xdate()
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()

# # You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert.
#
# file = 'Data/death_valley_2018_simple.csv'
# with open(file) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     # The enumerate() function returns both the index of each item and the value of each item as you loop through a list
#     # for index, column_header in enumerate(header_row):
#     #     print(index, column_header)
#
#     # getting rainfall from file
#     dates, rains = [], []
#
#     for data in reader:
#         current_date = datetime.strptime(data[2], '%Y-%m-%d')
#         rain = float(data[3])
#         dates.append(current_date)
#         rains.append(rain)
#
# # plot High temp
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, rains, c='blue')
#
# # Format plot
# plt.title("daily rainfall amounts 2018", fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel('Rainfall (inch)', fontsize=16)
# fig.autofmt_xdate()
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()

# # 16-2. Sitka–Death Valley Comparison: The temperature scales on the Sitka and Death Valley graphs reflect
# # the different data ranges. To accurately compare the temperature range in Sitka to that of Death Valley,
# # you need identical scales on the y-axis. Change the settings for the y-axis on one or both of the charts in
# # Figures 16-5 and 16-6. Then make a direct comparison between temperature ranges in Sitka and Death Valley
# # (or any two places you want to compare).
#
# file = 'Data/sitka_weather_2018_simple.csv'
# with open(file) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     # print(header_row)
#
#     # The enumerate() function returns both the index of each item and the value of each item as you loop through a list
#     # for index, column_header in enumerate(header_row):
#     #     print(index, column_header)
#
#     # getting high temp from file
#     dates, highs, lows = [], [], []
#
#     for data in reader:
#         current_date = datetime.strptime(data[2], '%Y-%m-%d')
#         high = int(data[5])
#         low = int(data[6])
#         dates.append(current_date)
#         highs.append(high)
#         lows.append(low)
#
# # plot High&low temp
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, c='red', alpha=0.5)
# ax.plot(dates, lows, c='blue', alpha=0.5)
# # Shading an Area in the Chart
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
# # Format plot
# plt.title("Daily high & low temperatures - 2018", fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel('Temperature (F)', fontsize=16)
# fig.autofmt_xdate()
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.ylim(20, 130)
#
# plt.show()

##################################################


# def get_weather_data(file, dates, highs, lows, date_index, high_index, low_index):
#     with open(file) as f:
#         reader = csv.reader(f)
#         header_row = next(reader)
#     # getting high temp from file
#         for data in reader:
#             current_date = datetime.strptime(data[date_index], '%Y-%m-%d')
#             try:
#                 high = int(data[high_index])
#                 low = int(data[low_index])
#             except ValueError:
#                 print(f"Missing data for {current_date}")
#             else:
#                 dates.append(current_date)
#                 highs.append(high)
#                 lows.append(low)
#
#
# # plot sitka High&low temp
# file = 'Data/sitka_weather_2018_simple.csv'
# dates, highs, lows = [], [], []
# get_weather_data(file, dates, highs, lows, date_index=2, high_index=5, low_index=6)
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, c='red', alpha=0.5)
# ax.plot(dates, lows, c='blue', alpha=0.5)
# # Shading an Area in the Chart
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
# # plot death valley temp
# file = 'Data/death_valley_2018_simple.csv'
# dates, highs, lows = [], [], []
# get_weather_data(file, dates, highs, lows, date_index=2, high_index=4, low_index=5)
# plt.style.use('seaborn')
# ax.plot(dates, highs, c='red', alpha=0.5)
# ax.plot(dates, lows, c='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
# # Format plot
# title = "Daily high and low temperatures - 2018"
# title += "\nSitka, AK and Death Valley, CA"
# plt.title(title, fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel('Temperature (F)', fontsize=16)
# fig.autofmt_xdate()
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.ylim(20, 130)
#
# plt.show()

# # 16-3. San Francisco: Are temperatures in San Francisco more like temperatures in Sitka or
# # temperatures in Death Valley? Download some data for San Francisco, and generate a high-low temperature
# # plot for San Francisco to make a comparison.
#
# def get_weather_data(file, dates, highs, lows, date_index, high_index, low_index):
#     with open(file) as f:
#         reader = csv.reader(f)
#         header_row = next(reader)
#     # getting high temp from file
#         for data in reader:
#             current_date = datetime.strptime(data[date_index], '%Y-%m-%d')
#             try:
#                 high = int(data[high_index])
#                 low = int(data[low_index])
#             except ValueError:
#                 print(f"Missing data for {current_date}")
#             else:
#                 dates.append(current_date)
#                 highs.append(high)
#                 lows.append(low)
#
#
# # plot sitka High&low temp
# file = 'Data/sitka_weather_2018_simple.csv'
# dates, highs, lows = [], [], []
# get_weather_data(file, dates, highs, lows, date_index=2, high_index=5, low_index=6)
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, c='red', alpha=0.5)
# ax.plot(dates, lows, c='blue', alpha=0.5)
# # Shading an Area in the Chart
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
# # # plot death valley temp
# # file = 'Data/death_valley_2018_simple.csv'
# # dates, highs, lows = [], [], []
# # get_weather_data(file, dates, highs, lows, date_index=2, high_index=4, low_index=5)
# # plt.style.use('seaborn')
# # ax.plot(dates, highs, c='red', alpha=0.5)
# # ax.plot(dates, lows, c='blue', alpha=0.5)
# # ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
# # # plot california temp
# file = 'Data/california.csv'
# dates, highs, lows = [], [], []
# get_weather_data(file, dates, highs, lows, date_index=2, high_index=4, low_index=5)
# plt.style.use('seaborn')
# ax.plot(dates, highs, c='red', alpha=0.5)
# ax.plot(dates, lows, c='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
# # Format plot
# title = "Daily high and low temperatures - 2018"
# title += "\nSitka, AK and Death Valley, CA"
# plt.title(title, fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel('Temperature (F)', fontsize=16)
# fig.autofmt_xdate()
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.ylim(20, 130)
#
# plt.show()

