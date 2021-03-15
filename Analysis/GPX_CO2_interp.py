#%% Python libraries--don't edit

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

import gpxpy

plt.close('all')
#%% Inputs:
# YOU CAN/SHOULD MODIFY FILENAMES AS NEEDED
# MAKE SURE EXTENSION IS WRITTEN EXACTLY AS IT SHOWS UP ON YOUR COMPUTER
# (e.g., .csv or .CSV, .gpx, .GPX)

# Filename for CO2 data
# CO2 data should be a .csv file and ONLY the data from one particular experiment
# Trim data in Excel first and save again as .CSV if needed (not .TXT)
CO2_filename = 'K30_0000.csv'

# Time when I noted that CO2 logging began *** in UTC ***
# Year, month, day, hour (24 hr format), minute, second
starttime_utc = datetime.datetime(2021, 3, 8, 12, 47, 0)

# Strava GPX file
gpx_filename = 'CO2_sensor_test_walk.gpx'


#%% Read in CO2 data
df_CO2 = pd.read_csv(CO2_filename)
elapsed_time_sec = df_CO2.iloc[:, 0] # insensitive to column name
CO2 = df_CO2.iloc[:, 1]

#%% Calculate "absolute" rather than elapsed time for CO2 sensor, in UTC
# time_CO2 = starttime_utc+pd.Timedelta(seconds = elapsed_time_sec)
time_CO2 = [starttime_utc+datetime.timedelta(seconds = e_time) for e_time in elapsed_time_sec]
time_CO2 = pd.Series(time_CO2)

# Add newly named and calculated columns to original DataFrame, reset index to time in UTC
df_CO2['Time (UTC)'] = time_CO2
df_CO2.set_index('Time (UTC)', inplace = True, drop = True)
df_CO2['CO2 (ppm)']

#%% GPS
################################################################################
# Add Garmin GPS data
################################################################################
lat_strava = []
lon_strava = []
time_strava = []
points = []

# Extract time, lat, and lon from .GPX file
gpx_file = open(gpx_filename, 'r')
gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            lat_strava.append(point.latitude)
            lon_strava.append(point.longitude)
            time_strava.append(pd.to_datetime(point.time))
            points.append(tuple([point.latitude, point.longitude]))

data_strava = {'lat': lat_strava, 'lon': lon_strava}
df_strava = pd.DataFrame(data_strava, index = time_strava)
df_strava.index = df_strava.index.tz_localize(None)

#%% Plot current data
fig, axs = plt.subplots()
axs.plot(df_CO2.index, df_CO2['CO2 (ppm)'], 'ko-')
axs.plot(df_CO2.index[0::5], df_CO2['CO2 (ppm)'][0::5], 'ro-')
axs.set_xlabel('Time (UTC)')
axs.set_ylabel('CO2 (ppm)')
axs.set_title('CO2 vs. Time')
fig.autofmt_xdate()

# Plot timestamps only to see if they align
fig, axs = plt.subplots()
axs.plot(df_CO2.index, df_CO2.index, 'k.-', label = 'K-30')
axs.plot(df_strava.index[0::5], df_strava.index[0::5], 'r.', label = 'Strava')
fig.legend()

#%% Merge CO2 and Strava Data
# Merge to get lat/lon alongside CO2
df_merge = pd.merge(df_CO2, df_strava, left_index = True, right_index = True)
df_merge.to_csv('merged_CO2_and_GPS.csv')