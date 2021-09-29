import csv
import matplotlib.pyplot as plt 
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter= ",")

header_row = next(csv_file)

#print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index,column_header)

#Testing to convert date from string 
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(mydate)


dates = []
highs = []
lows = []

for i in csv_file:

    try:
        the_date = datetime.strptime(i[2], '%Y-%m-%d')
        high = int(i[4])
        low = int(i[4])
        
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)


#print(highs)
#print(dates)
#print(lows)



fig = plt.figure()

plt.title("Daily high and low temperature - 2018\nDeath valley", fontsize = 16)
plt.xlabel("YKTV", fontsize = 12)
plt.ylabel("temperature (f)", fontsize = 12)
plt.tick_params(axis = "both", which = "major", labelsize = 12)

plt.plot(dates,highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)

plt.fill_between(dates,highs,lows, facecolor = 'blue', alpha = 0.1)

fig.autofmt_xdate()


plt.show()


plt.subplot(2,1,1)
plt.plot(dates,highs, c = 'red')
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows , c = 'blue')
plt.title("Lows")

#plt.subtitle()

plt.show()

