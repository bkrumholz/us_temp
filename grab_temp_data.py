import pandas as pd

day_col=[]
for i in range(1,32):
    day_col.append("Day_"+str(i))

print(day_col)
temp_col_name = ['Station','Line']+ day_col
print(temp_col_name)

weather_station = pd.read_fwf('Data/zipcodes-normals-stations.txt', colspecs='infer',names=['Station','ZIP','City'],dtype={'Station':str,'ZIP':str,'City':str})
temp_pd = pd.read_fwf('Data/dly-tmax-normal.txt', colspecs='infer',names=temp_col_name,dtype={'Station':str,'Line':int})


print(len(weather_station))
print(weather_station.head())
print(weather_station['City'][2])

print(temp_pd.head())
print(type(temp_pd['Station'][0]))

print(weather_station[weather_station['Station']=='AQW00061705'])
print(temp_pd[temp_pd['Station']=='AQW00061705'])

new_pd = temp_pd.merge(weather_station, on='Station', how='left')

# Find joined lines that are found
print(new_pd[pd.isna(new_pd['ZIP']) == False].head())

print(temp_pd.head())