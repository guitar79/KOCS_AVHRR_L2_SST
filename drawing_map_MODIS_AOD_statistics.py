'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Created on Sat Nov  3 20:34:47 2018
@author: guitar79
created by Kevin 

#basemap
conda install -c conda-forge basemap-data-hires
conda install -c conda-forge basemap
'''

from glob import glob
import numpy as np
from datetime import datetime
import calendar
import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#for checking time
cht_start_time = datetime.now()

dir_name = 'DAAC_MOD04_3K/all/'
save_dir_name = 'DAAC_MOD04_3K/save/'
if not os.path.exists(save_dir_name):
    os.makedirs(save_dir_name)
    print ('*'*80)
    print (save_dir_name, 'is created')
else :
    print ('*'*80)
    print (save_dir_name, 'is exist')

#JulianDate_to_date(2018, 131) -- '20180511'
def JulianDate_to_date(y, jd):
    month = 1
    while jd - calendar.monthrange(y,month)[1] > 0 and month <= 12:
        jd = jd - calendar.monthrange(y,month)[1]
        month += 1
    #return datetime(y, month, jd).strftime('%Y%m%d')
    return datetime(y, month, jd)

#date_to_JulianDate('20180201', '%Y%m%d') -- 2018032
def date_to_JulianDate(dt, fmt):
    dt = datetime.strptime(dt, fmt)
    tt = dt.timetuple()
    return int('%d%03d' % (tt.tm_year, tt.tm_yday))

#for modis hdf file, filename = 'DAAC_MOD04_3K/H28V05/MOD04_3K.A2014003.0105.006.2015072123557.hdf'
def filename_to_datetime(filename):
    fileinfo = filename.split('.')
    #print('fileinfo', fileinfo)
    return JulianDate_to_date(int(fileinfo[1][1:5]), int(fileinfo[1][5:8]))

    
f_name = 'AOD_3K_20150728_20150805_90_150_10_60_0.1.npy'
hdf_data = np.load(save_dir_name+f_name)
lon_array = hdf_data[0,:,:]
lat_array = hdf_data[1,:,:]
aod = hdf_data[2,:,:]
Llon = np.min(hdf_data[0,:,:])
Rlon = np.max(hdf_data[0,:,:])
Slat = np.min(hdf_data[1,:,:])
Nlat = np.max(hdf_data[1,:,:])

#Plot data on the map
#print('='*80)
#print(datetime.now(), proc_start_date, '-', proc_end_date, 'Plotting data on the map')
plt.figure(figsize=(10, 10))
# sylender map
m = Basemap(projection='cyl', resolution='h', \
            llcrnrlat = Slat, urcrnrlat = Nlat, \
            llcrnrlon = Llon, urcrnrlon = Rlon)
m.drawcoastlines(linewidth=0.25)
m.drawcountries(linewidth=0.25)

#m.fillcontinents(color='coral',lake_color='aqua')
#m.drawmapboundary(fill_color='aqua')

m.drawparallels(np.arange(-90., 90., 10.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 15.), labels=[0, 0, 0, 1])

x, y = m(lon_array, lat_array) # convert to projection map

plt.pcolormesh(x, y, aod)
plt.colorbar(cmap='bwr', fraction=0.038, pad=0.04)

plt.title('MODIS AOD', fontsize=20)
plt.savefig(save_dir_name+f_name[:-4]+'.png', bbox_inches='tight', dpi = 300)
plt.savefig(save_dir_name+f_name[:-4]+'.pdf', bbox_inches='tight', dpi = 300)

plt.show()
