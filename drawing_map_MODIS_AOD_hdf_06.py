#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:47:09 2018

@author: guitar79
"""

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Created on Sat Nov  3 20:34:47 2018
@author: guitar79
created by Kevin 

#Open hdf file
NameError: name 'SD' is not defined
conda install -c conda-forge pyhdf=0.9.0
#basemap
conda install -c conda-forge basemap-data-hires
conda install -c conda-forge basemap
'''

from glob import glob
import numpy as np
from datetime import datetime
import calendar
import os
from pyhdf.SD import SD, SDC
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import threading
from queue import Queue

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

#f_name = 'MYD04_3K.A2016366.0440.006.2017010010311.hdf'

#write log file

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

#for modis hdf file
#filename = 'DAAC_MOD04_3K/H28V05/MOD04_3K.A2014003.0105.006.2015072123557.hdf'
def filename_to_datetime(filename):
    fileinfo = filename.split('.')
    #print('fileinfo', fileinfo)
    return JulianDate_to_date(int(fileinfo[1][1:5]), int(fileinfo[1][5:8]))

def f(proc_date):
    proc_start_date = proc_date[0]
    proc_end_date = proc_date[1]
    thread_number = proc_date[2]
    add_log = open(save_dir_name + proc_start_date + '_' + proc_end_date + '.log', 'a')
    # some variables for downloading (site, file, perid and time gap, etc.)
    start_date = datetime(int(proc_start_date[:4]), int(proc_start_date[4:6]), int(proc_start_date[6:8])) #convert startdate to date type
    end_date = datetime(int(proc_end_date[:4]), int(proc_end_date[4:6]), int(proc_end_date[6:8])) #convert startdate to date type
    #duration = (end_date - start_date).days + 1 #total days for working
    
    #print(datetime.now(), proc_start_date, '-', proc_end_date, 'Starting thread #', thread_number)
  
    #Set lon, lat, resolution
    Llon, Rlon = 90, 150
    Slat, Nlat = 10, 60
    resolution = 0.5
    #fac = 1./resolution
    
    #Make Grid
    print('='*80)
    print(datetime.now(), proc_start_date, '-', proc_end_date, 'Start making grid arrays...')
    add_log.write('%s: %s-%s Start making grid arrays...\n' % (datetime.now(), proc_start_date, proc_end_date))
    
    ni = np.int((Rlon-Llon)/resolution+1.00)
    nj = np.int((Nlat-Slat)/resolution+1.00)
    
    lon_array = []
    lat_array = []
    data_array = []   
    mean_array = [] 
    cnt_array = [] 
    for i in range(ni):
        lon_line = []
        lat_line = []
        data_line = []
        mean_line = [] 
        cnt_line = [] 
        for j in range(nj):
            lon_line.append(Llon+resolution*i)
            lat_line.append(Nlat-resolution*j)
            data_line.append([])
            mean_line.append([])
            cnt_line.append([])
        lon_array.append(lon_line)
        lat_array.append(lat_line)
        data_array.append(data_line)
        mean_array.append(mean_line)
        cnt_array.append(cnt_line)
    lat_array = np.array(lat_array)
    lon_array = np.array(lon_array)
    print('grid arrays are created\n')
    
    #data_array = np.array(data_array)
    print('='*80)
    #print(datetime.now(), proc_start_date, '-', proc_end_date, 'Finish making grid array...')
    working_time = (datetime.now() - cht_start_time) #total days for downloading
    print(datetime.now(), 'working time (sec) :', working_time)
    print('='*80) 
    
    
        
    cnt = 0
    kk=0
    
    for k in sorted(glob(os.path.join(dir_name, '*.hdf'))):
    
        result_array = data_array
        file_date = filename_to_datetime(k)
        #print('fileinfo', file_date)
        
        if file_date >= start_date \
            and file_date <= end_date : \
            
            print('='*80)
            #print(datetime.now(), proc_start_date, '-', proc_end_date, 'Start reading HDF file and extract Longitude, Latitude and AOD value', k)
            print(datetime.now(), 'Start reading HDF file and extract Longitude, Latitude and AOD value', k)
            add_log.write('%s: %s-%s %s...\n              Start reading HDF file and extract Longitude, Latitude and AOD value\n' % (datetime.now(), proc_start_date, proc_end_date, k))
            try:
                hdf = SD(k, SDC.READ)
                # Read AOD dataset.
                DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'
                hdf_raw = hdf.select(DATAFIELD_NAME)
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
            except:
                print("Something got wrecked \n")
                continue
            
            print('='*80)
            #print(datetime.now(), proc_start_date, '-', proc_end_date, longitude.min(), longitude.max(), latitude.min(), latitude.max())
    
            #print('Finish reading HDF file and extract Longitude, Latitude and AOD value')    
            print('='*80)
            
            print('='*80)
            print('Longitude, Latitude and AOD values will be insert to the grid', k)
            add_log.write('%s: %s-%s %s...\n              Longitude, Latitude and AOD values will be insert to the grid..\n' % (datetime.now(), proc_start_date, proc_end_date, k))
            if np.shape(longitude) != np.shape(latitude) or np.shape(latitude) != np.shape(aod) :
                print('data shape is different!!')
                print('='*80)
            else : 
                lon_cood = np.array(((longitude-Llon)/resolution*100//100), dtype=np.uint16)
                lat_cood = np.array(((Nlat-latitude)/resolution*100//100), dtype=np.uint16)
            
                for i in range(np.shape(lon_cood)[0]) :
                    for j in range(np.shape(lon_cood)[1]) :
                        if int(lon_cood[i][j]) < np.shape(lon_array)[0] \
                            and int(lat_cood[i][j]) < np.shape(lon_array)[1] \
                            and not np.isnan(aod[i][j]) :
                            cnt += 1 #for debug
                            #print('file : ', kk, 'cnt1 :' , cnt)
                            result_array[int(lon_cood[i][j])][int(lat_cood[i][j])].append(aod[i][j])
                print('='*80)
                print(datetime.now(), proc_start_date, '-', proc_end_date, 'Finish inserting Longitude, Latitude and AOD values to the grid')
                print('='*80)
                kk += 1
            print('file : ', kk, 'cnt1 :' , cnt)
            #if kk == 10 : break

        
    working_time = (datetime.now() - cht_start_time) #total days for downloading
    print(datetime.now(), 'working time (sec) :', working_time)
    print('='*80)   
      
    
    print('='*80)
    print(datetime.now(), proc_start_date, '-', proc_end_date, 'Calculating mean value at each pixel is being started ')
    add_log.write('%s: %s-%s Calculating mean value at each pixel is being started ...\n' % (datetime.now(), proc_start_date, proc_end_date))
    cnt2 = 0 #for debug
    for i in range(np.shape(result_array)[0]):
        for j in range(np.shape(result_array)[1]):
            cnt2 += 1 #for debug
            if len(result_array[i][j])>0: mean_array[i][j] = np.mean(result_array[i][j])
            else : mean_array[i][j] = np.nan
            cnt_array[i][j] = len(result_array[i][j])
        print(thread_number, 'cnt2 :' , cnt2)

    mean_array = np.array(mean_array)
    cnt_array = np.array(cnt_array)
    print(np.shape(mean_array))
    
    print('='*80)
    print(datetime.now(), proc_start_date, '-', proc_end_date, 'Calculating mean value at each pixel is finished ')
    print('='*80)
    add_log.write('%s: %s-%s Calculating mean value at each pixel is finished ...\n' % (datetime.now(), proc_start_date, proc_end_date))
    
    working_time = (datetime.now() - cht_start_time) #total days for downloading
    print(datetime.now(), 'working time (sec) :', working_time)
    print('='*80)   

    '''    
    sd = SD("hello.hdf", SDC.WRITE | SDC.CREATE)
    sds = sd.create("sds1", SDC.INT16, mean_array.shape)
    sds.setfillvalue(0)
    sds[:] = mean_array
    sds.endaccess()
    sd.end()

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
    
    plt.pcolormesh(x, y, mean_array)
    plt.colorbar(cmap='bwr', fraction=0.038, pad=0.04)
    
    plt.title('MODIS AOD \n (' + proc_start_date + '-' + proc_end_date + ')', fontsize=20)
    plt.savefig(save_dir_name+'_'+proc_start_date+'-'+proc_end_date+'.png', bbox_inches='tight', dpi = 300)
    '''
    
    working_time = (datetime.now() - cht_start_time) #total days for downloading
    #print(datetime.now(), proc_start_date, '-', proc_end_date, 'Map(image) is created ')
    add_log.write('%s: %s-%s Map(image) is created...\n' % (datetime.now(), proc_start_date, proc_end_date))
    print(datetime.now(), 'working time (sec) :', working_time)
    print('='*80) 
    print('Thread '+str(thread_number)+' finished')
    #plt.show()
    save_array = np.array([lon_array, lat_array, mean_array])
    np.save(save_dir_name+proc_start_date+'_'+proc_end_date+'.npy', save_array)
    print(save_dir_name+proc_start_date+'_'+proc_end_date+'.npy is creaated')
    return mean_array, cnt_array

print_lock = threading.Lock()

def process_queue():
    while True:
        file_data = compress_queue.get()
        f(file_data)
        compress_queue.task_done()

compress_queue = Queue()

dates = [('20150101', '20150131', 1), ('20150201', '20150228', 2), ('20150301', '20150331', 3),\
         ('20150401', '20150430', 4), ('20150501', '20150531', 5), ('20150601', '20150630', 6),\
         ('20150701', '20150731', 7), ('20150801', '20150831', 8), ('20150901', '20150930', 9),\
         ('201501001', '20151031', 10), ('20151101', '20151130', 11), ('20151201', '20151231', 12)]
         
'''
#https://datascienceschool.net/view-notebook/465066ac92ef4da3b0aba32f76d9750a/
#http://egloos.zum.com/mcchae/v/11203068
from dateutil.relativedelta import relativedelta

s_start_date = datetime(2015, 1, 1) #convert startdate to date type
s_end_date = datetime(2018, 12, 31)
s_delta1 = 'months'
s_delta = 1

edt = datetime.now() - relativedelta(months=3)
start_date = datetime(int(proc_start_date[:4]), int(proc_start_date[4:6]), int(proc_start_date[6:8])) #convert startdate to date type
end_date = datetime(int(proc_end_date[:4]), int(proc_end_date[4:6]), int(proc_end_date[6:8])) #convert startdate to date type
'''
num_cpu = 12

for i in range(num_cpu):
    t = threading.Thread(target=process_queue)
    t.daemon = True
    t.start()

for date in dates:
    compress_queue.put(date)

compress_queue.join()