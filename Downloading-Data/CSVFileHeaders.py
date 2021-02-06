import csv
import matplotlib.pyplot as plt
from datetime import datetime

file = 'Data/sitka_weather_07-2018_simple.csv'
with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # The enumerate() function returns both the index of each item and the value of each item as you loop through a list
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # getting high temp from file
    dates, highs = [], []

    for data in reader:
        current_date = datetime.strptime(data[2], '%Y-%m-%d')
        high = int(data[5])
        dates.append(current_date)
        highs.append(high)

print(highs)

# plot High temp
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
fig.autofmt_xdate()
# plt.tight_layout()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
