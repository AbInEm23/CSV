import csv
import matplotlib.pyplot as plt 
from datetime import datetime

#sitka
open_file_sitka = open("sitka_weather_2018_simple.csv", "r")
csv_file_sitka = csv.reader(open_file_sitka, delimiter= ",")
header_row_sitka = next(csv_file_sitka)
#death 
open_file_death = open("death_valley_2018_simple.csv", "r")
csv_file_death = csv.reader(open_file_death, delimiter= ",")
header_row_death= next(csv_file_death)

#header row for sitka
for index,column_header_sitka in enumerate(header_row_sitka):
    print(index,column_header_sitka)
   

#header row for death 
for index,column_header_death in enumerate(header_row_death):
    print(index,column_header_death)
    
#Testing to convert date from string 
#works for both
#mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(mydate)

#lists of sitka
dates_sitka = []
highs_sitka = []
lows_sitka = []
#index of sitka
sitka_index_for_high = header_row_sitka.index('TMAX')
sitka_index_for_low = header_row_sitka.index('TMIN')
sitka_index_for_date = header_row_sitka.index('DATE')
Sitka_title_index = header_row_sitka.index('NAME')

#lists of death
dates_death = []
highs_death = []
lows_death = []
#index of death
death_index_for_high = header_row_death.index('TMAX')
death_index_for_low = header_row_death.index('TMIN')
death_index_for_date = header_row_death.index('DATE')
death_title_index = header_row_death.index('NAME')

#append lists for sitka 
for i in csv_file_sitka:
    highs_sitka.append(int(i[sitka_index_for_high]))
    the_sitka_date = datetime.strptime(i[sitka_index_for_date], '%Y-%m-%d')
    dates_sitka.append(the_sitka_date)
    lows_sitka.append(int(i[sitka_index_for_low]))
    Name_of_sitka = i[Sitka_title_index]

#print(highs_sitka)
#print(dates_sitka)
#print(lows_sitka)


#append lists for death 
for i in csv_file_death:

    try:
        the_death_date = datetime.strptime(i[death_index_for_date], '%Y-%m-%d')
        high = int(i[death_index_for_high])
        low = int(i[death_index_for_low])
        Name_of_death = i[death_title_index]
        
    except ValueError:
        print(f"Missing data for {the_death_date}")
    else:
        highs_death.append(high)
        lows_death.append(low)
        dates_death.append(the_death_date)


fig = plt.figure()

plt.xlabel("Dates", fontsize = 12)
plt.ylabel("temperature (f)", fontsize = 12)
plt.tick_params(axis = "both", which = "major", labelsize = 12)

plt.subplot(2,1,1)
plt.plot(dates_sitka,highs_sitka, c = 'red')
plt.plot(dates_sitka,lows_sitka, c = 'blue')
plt.fill_between(dates_sitka,highs_sitka,lows_sitka, facecolor = 'blue', alpha = 0.1)
plt.title(Name_of_sitka)

plt.subplot(2,1,2)
plt.plot(dates_death,highs_death, c = 'red')
plt.plot(dates_death,lows_death, c = 'blue')
plt.fill_between(dates_death,highs_death,lows_death, facecolor = 'blue', alpha = 0.1)
plt.title(Name_of_death)

plt.suptitle(f"Temperature comparison between {Name_of_sitka} and {Name_of_death}")


fig.autofmt_xdate()
plt.show()




