'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Created on Sat Nov  3 20:34:47 2018
@author: guitar79
created by Kevin 
'''

from glob import glob
import numpy as np
from datetime import datetime
import os
import threading
from queue import Queue

#fo checking time
cht_start_time = datetime.now()

dir_name = '2011/'
save_dir_name = 'daily/'
save_file_header = 'KOSC_AVHRR_SST_'

if not os.path.exists(save_dir_name):
    os.makedirs(save_dir_name)
    print ('*'*80)
    print (save_dir_name, 'is created\n')
else :
    print ('*'*80)
    print (save_dir_name, 'is exist\n')

#for KOSC AVHRR sst file filename = '2011/2011.1117.1151.noaa-16.sst.asc'
def filename_AVHRR_to_fileinfo(filename):
    filename_el = filename.split('.')
    #print('filename_el', filename_el)
    filedatetime = datetime(int(filename_el[-6][-4:]), int(filename_el[-5][0:2]), int(filename_el[-5][2:4]),\
                   int(filename_el[-4][0:2]), int(filename_el[-4][2:4]) ) 
    satellite_name = filename_el[-3]
    return filedatetime, satellite_name

def f(proc_date):
    print('proc_date', proc_date)
    proc_start_date = proc_date[0]
    proc_end_date = proc_date[1]
    thread_number = proc_date[2]
    print('type(proc_start_date)', type(proc_start_date))
    print('type(proc_end_date)', type(proc_end_date))
    
    write_log = '#This file is created using python \n' \
                '#https://github.com/guitar79/KOCS_AVHRR_L2_SST \n' \
                + '#start date = ' + proc_date[0] +'\n'\
                + '#end date = ' + proc_date[1] +'\n'
    
    # some variables for downloading (site, file, perid and time gap, etc.)
    #convert startdate to date type
    start_date = datetime(int(proc_start_date[0:4]), int(proc_start_date[4:6]), int(proc_start_date[6:8])) 
    #convert startdate to date type
    end_date = datetime(int(proc_end_date[0:4]), int(proc_end_date[4:6]), int(proc_end_date[6:8])) 
  
    #Set lon, lat, resolution
    Llon, Rlon = 90, 150
    Slat, Nlat = 10, 60
    resolution = 0.25
    
    write_log += '#Llon =' + str(Llon) + '\n' \
                + '#Rlon =' + str(Rlon) + '\n' \
                + '#Slat =' + str(Slat) + '\n' \
                + '#Nlat =' + str(Nlat) + '\n' \
                + '#resolution =' + str(resolution) + '\n' 
    
    #Make Grid
    print('='*80)
    print(start_date, '-', end_date, 'Start making grid arrays...\n')
    
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
    print('grid arrays are created')
    print('='*80)
        
    total_data_cnt = 0
    file_no=0
    write_log += '#processing file list\n' + 'No, filename, data \n'
    
    for k in sorted(glob(os.path.join(dir_name, '*.asc'))):
        result_array = data_array
        file_date, satellite_name = filename_AVHRR_to_fileinfo(k)
                
        if file_date >= start_date \
            and file_date < end_date : 
            print('='*80)
            print(datetime.now(), 'Start reading asc file...\n', k)
            try:
                tsv_list = np.genfromtxt(k, delimiter="\t") 
                latitude = tsv_list[:,1]
                longitude = tsv_list[:,2]
                sst = tsv_list[:,3]
            except:
                print("Something got wrecked \n")
                continue
                        
            print('='*80)
            print('Starting... ', k)
            
            #if np.shape(longitude) != np.shape(latitude) or np.shape(latitude) != np.shape(sst) :
            if len(longitude) != len(latitude) or len(latitude) != len(sst) :
                print('data shape is different!! \n')
                print('='*80)
            else : 
                lon_cood = np.array(((longitude-Llon)/resolution*100//100), dtype=np.uint16)
                lat_cood = np.array(((Nlat-latitude)/resolution*100//100), dtype=np.uint16)
                data_cnt = 0
                print (np.shape(lon_cood))
            
                for i in range(np.shape(lon_cood)[0]) :
                    if int(lon_cood[i]) < np.shape(lon_array)[0] \
                        and int(lat_cood[i]) < np.shape(lon_array)[1] \
                        and not np.isnan(sst[i]) :
                        data_cnt += 1 #for debug
                        result_array[int(lon_cood[i])][int(lat_cood[i])].append(sst[i])
                file_no += 1
                total_data_cnt += data_cnt
            write_log += str(file_no) + ',' + str(data_cnt) +',' + str(k) + '\n'
            print('number of files: ', file_no, 'tatal data cnt :' , data_cnt)
    write_log += '#total data number =' + str(total_data_cnt) + '\n'
    print('='*80)
    print(start_date, '-', end_date, 'Calculating mean value at each pixel is being started ')
    
    cnt2 = 0 #for debug
    for i in range(np.shape(result_array)[0]):
        for j in range(np.shape(result_array)[1]):
            cnt2 += 1 #for debug
            if len(result_array[i][j]) > 0 : mean_array[i][j] = np.mean(result_array[i][j])
            else : mean_array[i][j] = np.nan
            cnt_array[i][j] = len(result_array[i][j])
    print(thread_number, 'cnt2 :' , cnt2)
    
    mean_array = np.array(mean_array)
    cnt_array = np.array(cnt_array)    
    save_array = np.array([lon_array, lat_array, mean_array])
    np.save(save_dir_name + save_file_header + proc_start_date + '_' + proc_end_date\
            + '_' + str(Llon) + '_' + str(Rlon) \
            + '_' + str(Slat) + '_' + str(Nlat)\
            + '_' + str(resolution) + '.npy', save_array)
    print(save_dir_name + save_file_header + proc_start_date + '_' + proc_end_date\
            + '_' + str(Llon)+'_'+str(Rlon)\
            +'_'+str(Slat)+'_'+str(Nlat)+'_'+str(resolution)+'.npy is creaated\n')
    with open('%s%S%s_%s_%s_%s_%s_%s_%s_info.txt' \
              % (save_dir_name, save_file_header, proc_start_date, proc_end_date,\
              str(Llon), str(Rlon), str(Slat), str(Nlat), str(resolution)), 'w') as f:
        f.write(write_log)
    print('='*80) 
    print('Thread '+str(thread_number)+' finished')
    return mean_array, cnt_array

print_lock = threading.Lock()

def process_queue():
    while True:
        file_data = compress_queue.get()
        f(file_data)
        compress_queue.task_done()

compress_queue = Queue()

#https://datascienceschool.net/view-notebook/465066ac92ef4da3b0aba32f76d9750a/
#http://egloos.zum.com/mcchae/v/11203068
from dateutil.relativedelta import relativedelta
s_start_date = datetime(2011, 9, 1) #convert startdate to date type
s_end_date = datetime(2011, 12, 31)

k=0
date1 = s_start_date
date2 = s_start_date
dates = []
while date2 < s_end_date : 
    k += 1
    #date2 = date1 + relativedelta(months=1)
    date2 = date1 + relativedelta(days=1)
    
    date1_strf = date1.strftime('%Y%m%d')
    date2_strf = date2.strftime('%Y%m%d')
    date = (date1_strf, date2_strf, k)
    dates.append(date)
    date1 = date2

num_cpu = 6

for i in range(num_cpu):
    t = threading.Thread(target=process_queue)
    t.daemon = True
    t.start()

for date in dates :
    compress_queue.put(date)

compress_queue.join()
