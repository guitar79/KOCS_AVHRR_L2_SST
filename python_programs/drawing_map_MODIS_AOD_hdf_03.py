#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:34:47 2018

@author: guitar79
"""

''' created by Kevin 
 Open hdf file
conda update-all
NameError: name 'SD' is not defined
conda install -c conda-forge pyhdf=0.9.0
conda install -c conda-forge basemap-data-hires
conda install -c conda-forge basemap
'''

import numpy as np
from datetime import datetime
import calendar
import os
from pyhdf.SD import SD, SDC
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from numpy import meshgrid


# some variables for downloading (site, file, perid and time gap, etc.)
startdate = '20150101' #start date
enddate = '20181010' #end date
time_gap = 6 #time gap
request_hour = range(0,24,time_gap) #make list
#request_hour = [0, 3, 6, 9, 12, 15, 18, 21] #make list


def JulianDate_to_date(y, jd):
    month = 1
    while jd - calendar.monthrange(y,month)[1] > 0 and month <= 12:
        jd = jd - calendar.monthrange(y,month)[1]
        month += 1
    return datetime(y, month, jd).strftime('%Y%m%d')
#JulianDate_to_date(2018, 131) -- '20180511'

def date_to_JulianDate(dt, fmt):
    dt = datetime.strptime(dt, fmt)
    tt = dt.timetuple()
    return int('%d%03d' % (tt.tm_year, tt.tm_yday))
#date_to_JulianDate('20180201', '%Y%m%d') -- 2018032

print('='*80)
print('Start making grid arrays...')
#Make Grid
Llon, Rlon = 90, 150
Slat, Nlat = 10, 60
resolution = 0.1
fac = 1./resolution

ni = np.int((Rlon-Llon)/resolution+1.00)
nj = np.int((Nlat-Slat)/resolution+1.00)

lon_array = []
lat_array = []
data_array = []   
mean_array = [] 
for i in range(ni):
    lon_line = []
    lat_line = []
    data_line = []
    mean_line = [] 
    for j in range(nj):
        lon_line.append(Llon+resolution*j)
        lat_line.append(Slat+resolution*i)
        data_line.append([])
        mean_line.append([])
    lon_array.append(lon_line)
    lat_array.append(lat_line)
    data_array.append(data_line)
    mean_array.append(mean_line)
lon_array = np.array(lon_array)
lat_array = np.array(lat_array)
print('='*80)
print('Finish making grid array...')
#data_array = np.array(data_array)
    
dir_name = 'DAAC_MOD04_3K/H28V05/'
f_name = 'MYD04_3K.A2016366.0440.006.2017010010311.hdf'

print('='*80)
print('Start reading HDF file and extract Longitude, Latitude and AOD value')
hdf = SD(dir_name+f_name, SDC.READ)
DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'
hdf_raw = hdf.select(DATAFIELD_NAME)
aod_data = hdf_raw[:,:]
scale_factor = hdf_raw.attributes()['scale_factor']
add_offset = hdf_raw.attributes()['add_offset']
aod = aod_data * scale_factor + add_offset
aod[aod < 0] = np.nan
aod = np.asarray(aod)

# Read geolocation dataset.
lon = hdf.select('Longitude')
longitude = lon[:,:]
lat = hdf.select('Latitude')
latitude = lat[:,:]
print('='*80)
print('Finish reading HDF file and extract Longitude, Latitude and AOD value')


print('='*80)
print('Longitude, Latitude and AOD values will be insert to the grid')
cnt = 0 #for debug
if np.shape(longitude) != np.shape(latitude) or np.shape(latitude) != np.shape(aod) :
    print('data shape is different!!')
else : 
    for i in range(np.shape(longitude)[0]) :
        for j in range(np.shape(longitude)[1]) :
            ii = int((longitude[i][j]-Llon)/resolution)
            jj = int((latitude[i][j]-Slat)/resolution)
            if ii <= np.shape(data_array)[0] \
                and jj <= np.shape(data_array)[1] \
                and aod[i][j] is not np.nan :
                cnt += 1 #for debug
                print('cnt:', cnt) #for debug
                data_array[ii][jj].append(aod[i][j])
print('='*80)
print('Finish inserting Longitude, Latitude and AOD values to the grid')


print('='*80)
print('Start calculate mean value ')
for i in range(np.shape(data_array)[0]):
    for j in range(np.shape(data_array)[1]):
        mean_array[i][j] = np.mean(data_array[i][j])
print('='*80)
print('Finish calculate mean value ')


mean_array = np.array(mean_array)

print('='*80)
print('Draw picture')        
#Draw map
plt.figure(figsize=(10, 10))

# sylender map
m = Basemap(projection='cyl', resolution='h', \
            llcrnrlat = Slat, urcrnrlat = Nlat, \
            llcrnrlon=Llon, urcrnrlon = Rlon)
m.drawcoastlines(linewidth=0.25)
m.drawcountries(linewidth=0.25)
#m.fillcontinents(color='coral',lake_color='aqua')
#m.drawmapboundary(fill_color='aqua')
m.drawparallels(np.arange(-90., 90., 10.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 15.), labels=[0, 0, 0, 1])

x, y = m(lon_array, lat_array) # convert to projection map

plt.pcolormesh(x, y, mean_array)
plt.colorbar(cmap='bwr', fraction=0.038, pad=0.04)

plt.title('MODIS AOD', fontsize=20)
plt.savefig(dir_name+f_name+'.png', bbox_inches='tight', dpi = 300)

plt.show()
