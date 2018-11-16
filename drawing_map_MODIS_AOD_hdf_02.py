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

#Make Grid
Slat, Nlat = 10, 60
Llon, Rlon = 90, 150
resolution = 0.02
fac = 1./resolution

def make_grid(Slat, Nlat, Llon, Rlon, resolution) :
    ni = np.int((Nlat-Slat)/resolution+1)
    nj = np.int((Rlon-Llon)/resolution+1)
    
    lat_array = []
    lon_array = []
    data_array = []   
    mean_array = [] 
    for i in range(ni):
        lat_line = []
        lon_line = []
        data_line = []
        mean_line = [] 
        for j in range(nj):
            lat_line.append(Slat+resolution*i)
            lon_line.append(Llon+resolution*j)
            data_line.append([])
            mean_line.append([])
        lat_array.append(lat_line)
        lon_array.append(lon_line)
        data_array.append(data_line)
        mean_array.append(mean_line)
    lat_array = np.array(lat_array)
    lon_array = np.array(lon_array)
    print('grid arrays are created')
    #data_array = np.array(data_array)
    return lat_array, lon_array, data_array, mean_array


dir_name = 'DAAC_MOD04_3K/H28V05/'
f_name = 'MYD04_3K.A2016366.0440.006.2017010010311.hdf'

def read_hdf_aoddata(fname):
    hdf = SD(dir_name+f_name, SDC.READ)
    #print (hdf.datasets())
    #print (dir(hdf))
    # List available SDS datasets.
    #{'Longitude': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 5, 0), 'Latitude': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 5, 1), 'Scan_Start_Time': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 6, 2), 'Solar_Zenith': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 3), 'Solar_Azimuth': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 4), 'Sensor_Zenith': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 5), 'Sensor_Azimuth': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 6), 'Scattering_Angle': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 7), 'Glint_Angle': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 8), 'Land_Ocean_Quality_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 9), 'Land_sea_Flag': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 10), 'Wind_Speed_Ncep_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 11), 'Optical_Depth_Land_And_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 12), 'Image_Optical_Depth_Land_And_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 13), 'Aerosol_Type_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 14), 'Fitting_Error_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 15), 'Surface_Reflectance_Land': (('Solution_2_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 676, 451), 22, 16), 'Corrected_Optical_Depth_Land': (('Solution_3_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (3, 676, 451), 22, 17), 'Corrected_Optical_Depth_Land_wav2p1': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 18), 'Optical_Depth_Ratio_Small_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 19), 'Number_Pixels_Used_Land': (('Solution_1_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 20), 'Mean_Reflectance_Land': (('MODIS_Band_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 21), 'STD_Reflectance_Land': (('MODIS_Band_Land:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 22), 'Mass_Concentration_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 5, 23), 'Aerosol_Cloud_Fraction_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 24), 'Quality_Assurance_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04', 'QA_Byte_Land:mod04'), (676, 451, 5), 20, 25), 'Solution_Index_Ocean_Small': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 26), 'Solution_Index_Ocean_Large': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 27), 'Effective_Optical_Depth_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 28), 'Effective_Optical_Depth_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 29), 'Optical_Depth_Small_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 30), 'Optical_Depth_Small_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 31), 'Optical_Depth_Large_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 32), 'Optical_Depth_Large_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 33), 'Mass_Concentration_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 5, 34), 'Aerosol_Cloud_Fraction_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 35), 'Effective_Radius_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 36), 'PSML003_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 5, 37), 'Asymmetry_Factor_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 38), 'Asymmetry_Factor_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 39), 'Backscattering_Ratio_Best_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 40), 'Backscattering_Ratio_Average_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 41), 'Angstrom_Exponent_1_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 42), 'Angstrom_Exponent_2_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 43), 'Least_Squares_Error_Ocean': (('Solution_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (2, 676, 451), 22, 44), 'Optical_Depth_Ratio_Small_Ocean_0.55micron': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 45), 'Optical_Depth_by_models_ocean': (('Solution_Index:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (9, 676, 451), 22, 46), 'Number_Pixels_Used_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 47), 'Mean_Reflectance_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 48), 'STD_Reflectance_Ocean': (('MODIS_Band_Ocean:mod04', 'Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (7, 676, 451), 22, 49), 'Quality_Assurance_Ocean': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04', 'QA_Byte_Ocean:mod04'), (676, 451, 5), 20, 50), 'Topographic_Altitude_Land': (('Cell_Along_Swath:mod04', 'Cell_Across_Swath:mod04'), (676, 451), 22, 51)}
    
    # Read AOD dataset.
    DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'
    hdf_raw = hdf.select(DATAFIELD_NAME)
    #print(dir(hdf_raw))
    #print(dir(hdf_raw.dimensions()))
    #aod_attri = hdf_raw.attributes()
    #print('aod_attri', aod_attri)
    aod_data = hdf_raw[:,:]
    scale_factor = hdf_raw.attributes()['scale_factor']
    add_offset = hdf_raw.attributes()['add_offset']
    aod = aod_data * scale_factor + add_offset
    aod[aod < 0] = np.nan
    aod = np.asarray(aod)
    
    # Read geolocation dataset.
    lat = hdf.select('Latitude')
    latitude = lat[:,:]
    lon = hdf.select('Longitude')
    longitude = lon[:,:]
    return latitude, longitude, aod

def aoddata_to_grid(latitude, longitude, aod, data_array):

    #cnt = 0 #for debus
    if np.shape(longitude) != np.shape(latitude) or np.shape(latitude) != np.shape(aod) :
        print('data shape is different!!')
    else : 
        for i in range(np.shape(longitude)[0]) :
            for j in range(np.shape(longitude)[1]) :
                 #print (format(array_data[ii][jj]['latitude'], '.2f'), int(latitude[i][j]*100)/100)
                 #print(latitude[i][j], latitude[i][j]-Slat)
                 ii = int((latitude[i][j]-Slat)/resolution)
                 #print(ii)
                 #print(longitude[i][j], longitude[i][j]-Llon)
                 jj = int((longitude[i][j]-Llon)/resolution)
                 #print(jj)
    
                 if ii <= np.shape(data_array)[0] \
                 and jj <= np.shape(data_array)[1] \
                 and aod[i][j] is not np.nan :
                    #cnt += 1 #for debug
                    #print('cnt:', cnt) #for debug
                    data_array[ii][jj].append(aod[i][j])
                    #np.append(data_array[ii][jj], aod[i][j], axis=0)
    return data_array

make_grid(Slat, Nlat, Llon, Rlon, resolution)
read_hdf_aoddata(f_name)
data_array = aoddata_to_grid(latitude, longitude, aod, data_array)
for i in range(np.shape(data_array)[0]):
    for j in range(np.shape(data_array)[1]):
        mean_array[i][j] = np.mean(data_array[i][j])
mean_array = np.array(mean_array)

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

#x, y = m(longitude, latitude)
x, y = m(lon_array, lat_array) # convert to projection map

plt.pcolormesh(x, y, mean_array)
plt.colorbar(cmap='bwr', fraction=0.038, pad=0.04)
#cbar.set_label('X+Y')


# add colorbar.
#fig.colorbar(m, location='bottom', pad="5%", set_label='mm')
#cbar.set_label('mm')

#m.contourf(lon_array, lat_array, mean_array1, 15, linewidths=1.5)

plt.title('MODIS AOD')
plt.savefig(dir_name+f_name+'.png', bbox_inches='tight', dpi = 300)

plt.show()
